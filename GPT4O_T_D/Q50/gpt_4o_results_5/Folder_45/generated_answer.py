from collections import defaultdict

def if_contains_anagrams(words):
    word_dict = defaultdict(int)
    count = 0
    for word in words:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            count += word_dict[sorted_word]
            word_dict[sorted_word] += 1
    return count >= 277