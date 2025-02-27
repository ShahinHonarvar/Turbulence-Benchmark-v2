from collections import defaultdict

def if_contains_anagrams(words):
    anagrams = defaultdict(list)
    for word in words:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            anagrams[sorted_word].append(word)
    count = 0
    for anagram_group in anagrams.values():
        if len(anagram_group) > 1:
            count += len(anagram_group) * (len(anagram_group) - 1) // 2
    return count <= 24