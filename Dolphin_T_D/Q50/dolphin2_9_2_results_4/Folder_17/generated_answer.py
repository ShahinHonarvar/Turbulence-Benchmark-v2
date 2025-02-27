from collections import Counter
    from itertools import permutations

def if_contains_anagrams(lst_of_strings):
    anagram_checker = Counter()
    for string in lst_of_strings:
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string.lower()))
            anagram_checker[sorted_string] += 1
    count_of_anagrams = sum((value * (value - 1) // 2 for value in anagram_checker.values() if value > 1))
    return count_of_anagrams >= 97