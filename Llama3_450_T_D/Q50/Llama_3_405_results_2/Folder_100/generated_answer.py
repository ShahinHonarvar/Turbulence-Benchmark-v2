from collections import defaultdict

def if_contains_anagrams(lst):
    anagram_dict = defaultdict(list)
    for word in lst:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            anagram_dict[sorted_word].append(word)
    anagram_count = sum((len(value) * (len(value) - 1) // 2 for value in anagram_dict.values() if len(value) > 1))
    return anagram_count >= 95