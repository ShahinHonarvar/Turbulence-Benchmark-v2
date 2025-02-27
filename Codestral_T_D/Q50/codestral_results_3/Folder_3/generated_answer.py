from collections import defaultdict

def if_contains_anagrams(lst):
    anagram_dict = defaultdict(list)
    for word in lst:
        if len(word) >= 3:
            anagram_dict[''.join(sorted(word.lower()))].append(word)
    anagram_count = sum((len(anagrams) * (len(anagrams) - 1) // 2 for anagrams in anagram_dict.values()))
    return anagram_count >= 30