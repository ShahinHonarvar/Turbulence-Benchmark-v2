from collections import defaultdict

def if_contains_anagrams(words):
    anagrams = defaultdict(list)
    for word in words:
        sorted_word = ''.join(sorted(word.lower()))
        if len(sorted_word) >= 3:
            anagrams[sorted_word].append(word)
    count = 0
    for anagram_list in anagrams.values():
        count += len(anagram_list) * (len(anagram_list) - 1) // 2
    return count >= 36