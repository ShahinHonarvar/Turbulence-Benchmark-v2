import itertools

def if_contains_anagrams(strings_list):
    anagrams = []
    for string in strings_list:
        sorted_string = ''.join(sorted(string.lower()))
        if len(sorted_string) >= 3:
            anagrams.append(sorted_string)
    anagram_groups = [list(group) for key, group in itertools.groupby(sorted(anagrams))]
    anagram_pairs = sum((len(group) * (len(group) - 1) // 2 for group in anagram_groups))
    return anagram_pairs >= 144