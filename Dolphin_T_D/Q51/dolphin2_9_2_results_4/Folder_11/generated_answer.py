from collections import Counter

def if_contains_anagrams(words):
    pairs = 0
    word_dict = {}
    for word in words:
        word_lower = word.lower()
        if len(word_lower) < 3:
            continue
        word_sorted = ''.join(sorted(word_lower))
        if word_sorted not in word_dict:
            word_dict[word_sorted] = [word]
        else:
            word_dict[word_sorted].append(word)
    for key, value in word_dict.items():
        if len(value) > 1:
            pairs += len(value) * (len(value) - 1) // 2
            if pairs >= 41:
                return True
    return False