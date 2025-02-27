import itertools

def if_contains_anagrams(string_list):
    anagrams_count = 0
    anagrams = []
    for string in string_list:
        sorted_string = sorted(string.lower())
        anagram = ''.join(sorted_string)
        if len(string) >= 3 and anagram not in anagrams:
            anagrams.append(anagram)
    anagrams_pairs = list(itertools.combinations(anagrams, 2))
    anagrams_count = sum((1 for pair in anagrams_pairs if pair[0] != pair[1]))
    return anagrams_count >= 36