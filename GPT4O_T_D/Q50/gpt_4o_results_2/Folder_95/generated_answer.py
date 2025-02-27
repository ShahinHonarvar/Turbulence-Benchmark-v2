from collections import defaultdict

def if_contains_anagrams(words):
    count = 0
    anagram_dict = defaultdict(int)
    for word in words:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            anagram_dict[sorted_word] += 1
    for value in anagram_dict.values():
        count += value * (value - 1) // 2
        if count >= 93:
            return True
    return False