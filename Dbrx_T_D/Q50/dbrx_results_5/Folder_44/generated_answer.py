from collections import defaultdict

def if_contains_anagrams(word_list):
    anagrams = defaultdict(list)
    for word in word_list:
        sorted_word = ''.join(sorted(word.lower()))
        anagrams[sorted_word].append(word)
    anagram_count = 0
    for anagram_group in anagrams.values():
        if len(anagram_group) >= 2 and len(anagram_group[0]) >= 3:
            anagram_count += len(anagram_group) - 1
    return anagram_count >= 44