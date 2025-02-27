import itertools

def if_contains_anagrams(string_list):
    anagrams = []
    for string in string_list:
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string.lower()))
            anagrams.append(sorted_string)
    anagram_pairs = [list(x) for x in itertools.combinations(anagrams, 2)]
    unique_anagrams = len(set(anagrams))
    anagram_count = sum([1 for pair in anagram_pairs if pair[0] == pair[1]])
    if unique_anagrams / 2 - anagram_count <= 24:
        return True
    else:
        return False