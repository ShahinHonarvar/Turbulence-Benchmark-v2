from collections import Counter

def if_contains_anagrams(lst):
    anagram_dict = {}
    for word in lst:
        lower_word = word.lower()
        if len(lower_word) < 3:
            continue
        sorted_word = ''.join(sorted(lower_word))
        if sorted_word in anagram_dict:
            anagram_dict[sorted_word] += 1
        else:
            anagram_dict[sorted_word] = 1
    anagram_pairs = 0
    for count in anagram_dict.values():
        anagram_pairs += count * (count - 1) // 2
    return anagram_pairs <= 464