from collections import defaultdict

def if_contains_anagrams(words):
    word_dict = defaultdict(int)
    for word in words:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            word_dict[sorted_word] += 1
    count = 0
    for value in word_dict.values():
        if value > 1:
            count += value * (value - 1) // 2
            if count >= 178:
                return True
    return False