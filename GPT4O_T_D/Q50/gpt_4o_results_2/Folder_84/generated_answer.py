from collections import defaultdict

def if_contains_anagrams(words):
    anagram_dict = defaultdict(int)
    count = 0
    for word in words:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            anagram_dict[sorted_word] += 1
    for anagram_count in anagram_dict.values():
        count += anagram_count * (anagram_count - 1) // 2
        if count >= 108:
            return True
    return False