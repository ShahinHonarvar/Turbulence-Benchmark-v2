from collections import Counter

def if_contains_anagrams(lst):
    count = 0
    anagram_dict = {}
    for word in lst:
        word_lower = word.lower()
        if len(word_lower) >= 3:
            sorted_word = ''.join(sorted(word_lower))
            if sorted_word not in anagram_dict:
                anagram_dict[sorted_word] = 1
            else:
                anagram_dict[sorted_word] += 1
    for key in anagram_dict:
        count += anagram_dict[key] * (anagram_dict[key] - 1) // 2
    return count >= 34