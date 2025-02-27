from collections import defaultdict

def if_contains_anagrams(lst):
    anagram_count = defaultdict(list)
    for word in lst:
        sorted_word = ''.join(sorted(word.lower()))
        if len(sorted_word) >= 3:
            anagram_count[sorted_word].append(word)
    count = 0
    for group in anagram_count.values():
        if len(group) > 1:
            count += len(group) * (len(group) - 1) // 2
    return count <= 24