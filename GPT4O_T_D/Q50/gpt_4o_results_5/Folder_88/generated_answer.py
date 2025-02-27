from collections import defaultdict

def if_contains_anagrams(lst):
    count = 0
    anagram_dict = defaultdict(list)
    for word in lst:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            anagram_dict[sorted_word].append(word)
    for anagrams in anagram_dict.values():
        pair_count = len(anagrams) * (len(anagrams) - 1) // 2
        count += pair_count
        if count >= 34:
            return True
    return False