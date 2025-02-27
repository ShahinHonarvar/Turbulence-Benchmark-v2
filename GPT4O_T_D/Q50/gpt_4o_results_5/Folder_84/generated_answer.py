from collections import defaultdict

def if_contains_anagrams(words):
    anagram_count = 0
    anagram_dict = defaultdict(list)
    for word in words:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            anagram_dict[sorted_word].append(word.lower())
    for group in anagram_dict.values():
        n = len(group)
        if n > 1:
            anagram_count += n * (n - 1) // 2
        if anagram_count >= 108:
            return True
    return False