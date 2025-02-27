import itertools

def if_contains_anagrams(string_list):
    anagrams = []
    for string in string_list:
        if len(string) < 3:
            continue
        sorted_string = ''.join(sorted(string.lower()))
        anagrams.append(sorted_string)
    anagrams_pairs = list(itertools.combinations(anagrams, 2))
    anagram_count = 0
    for pair in anagrams_pairs:
        if pair[0] == pair[1]:
            anagram_count += 1
    return anagram_count >= 19