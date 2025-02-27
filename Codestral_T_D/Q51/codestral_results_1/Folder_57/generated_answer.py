from collections import defaultdict

def if_contains_anagrams(lst):
    anagram_dict = defaultdict(list)
    for word in lst:
        lower_word = word.lower()
        if len(lower_word) >= 3:
            sorted_word = ''.join(sorted(lower_word))
            anagram_dict[sorted_word].append(word)
    anagram_count = sum((len(anagrams) * (len(anagrams) - 1) // 2 for anagrams in anagram_dict.values()))
    return anagram_count <= 74