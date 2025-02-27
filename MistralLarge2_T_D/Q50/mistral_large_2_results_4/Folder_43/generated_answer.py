from collections import defaultdict

def if_contains_anagrams(lst):
    anagram_dict = defaultdict(list)
    for word in lst:
        if len(word) >= 3:
            key = ''.join(sorted(word.lower()))
            anagram_dict[key].append(word)
    anagram_count = sum((1 for words in anagram_dict.values() if len(words) > 1))
    return anagram_count >= 61