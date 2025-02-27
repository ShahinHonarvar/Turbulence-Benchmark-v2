from collections import defaultdict

def if_contains_anagrams(words):
    anagram_groups = defaultdict(list)
    for word in words:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            anagram_groups[sorted_word].append(word)
    anagram_count = 0
    for group in anagram_groups.values():
        n = len(group)
        if n > 1:
            anagram_count += n * (n - 1) // 2
        if anagram_count >= 64:
            return True
    return False