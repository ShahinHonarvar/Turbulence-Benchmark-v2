from collections import defaultdict

def if_contains_anagrams(words):
    anagram_count = 0
    anagrams = defaultdict(int)
    for word in words:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            anagrams[sorted_word] += 1
    for count in anagrams.values():
        anagram_count += count * (count - 1) // 2
    return anagram_count >= 24