from collections import defaultdict

def if_contains_anagrams(words):
    anagram_groups = defaultdict(int)
    count = 0
    for word in words:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            anagram_groups[sorted_word] += 1
    for count_synonyms in anagram_groups.values():
        if count_synonyms > 1:
            count += count_synonyms * (count_synonyms - 1) // 2
    return count >= 19