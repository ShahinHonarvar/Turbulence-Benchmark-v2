import itertools

def if_contains_anagrams(string_list):
    anagrams = []
    for string in string_list:
        string = string.lower()
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string))
            anagrams.append(sorted_string)
    anagram_pairs = [list(x) for x in itertools.combinations(anagrams, 2) if x[0] == x[1]]
    if len(anagram_pairs) <= 81:
        return True
    else:
        return False