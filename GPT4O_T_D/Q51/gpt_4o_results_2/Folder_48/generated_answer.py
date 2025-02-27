from collections import defaultdict

def if_contains_anagrams(words):
    anagram_count = 0
    anagram_groups = defaultdict(list)
    for word in words:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            anagram_groups[sorted_word].append(word)
    for group in anagram_groups.values():
        n = len(group)
        anagram_count += n * (n - 1) // 2
        if anagram_count > 277:
            return False
    return True