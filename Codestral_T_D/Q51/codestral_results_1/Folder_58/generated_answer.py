from collections import Counter

def if_contains_anagrams(lst):
    anagram_dict = Counter()
    for word in lst:
        normalized_word = ''.join(sorted(word.lower()))
        if len(normalized_word) >= 3:
            anagram_dict[normalized_word] += 1
    anagram_pairs = sum((count * (count - 1) // 2 for count in anagram_dict.values()))
    return anagram_pairs <= 60