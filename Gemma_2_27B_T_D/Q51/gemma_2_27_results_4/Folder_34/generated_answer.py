from collections import defaultdict

def if_contains_anagrams(words):
    anagram_groups = defaultdict(list)
    for word in words:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            anagram_groups[sorted_word].append(word)
    count = 0
    for group in anagram_groups.values():
        count += len(group) * (len(group) - 1) // 2
    return count <= 401