from collections import defaultdict

def if_contains_anagrams(lst):
    anagram_dict = defaultdict(list)
    for word in lst:
        word_lower = word.lower()
        if len(word_lower) >= 3:
            sorted_word = ''.join(sorted(word_lower))
            anagram_dict[sorted_word].append(word_lower)
    count = 0
    for key in anagram_dict:
        length = len(anagram_dict[key])
        count += length * (length - 1) // 2
    return count >= 34