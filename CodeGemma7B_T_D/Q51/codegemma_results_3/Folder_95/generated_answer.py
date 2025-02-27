from collections import defaultdict

def if_contains_anagrams(str_list):
    anagram_groups = defaultdict(list)
    for string in str_list:
        letters = [ch for ch in string.lower() if ch.isalpha()]
        letters.sort()
        anagram_groups[tuple(letters)].append(string)
    return len(anagram_groups) <= 6