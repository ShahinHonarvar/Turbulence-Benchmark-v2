import itertools

def if_contains_anagrams(strings_list):
    anagrams = []
    for string in strings_list:
        sorted_string = ''.join(sorted(string.lower()))
        if len(sorted_string) >= 3:
            anagrams.append(sorted_string)
    anagram_pairs = [len(list(group)) for value, group in itertools.groupby(sorted(anagrams))]
    return sum(anagram_pairs) <= 69