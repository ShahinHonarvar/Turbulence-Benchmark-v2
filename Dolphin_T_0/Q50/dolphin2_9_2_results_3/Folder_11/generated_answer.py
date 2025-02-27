def if_contains_anagrams(list_of_strings):
    anagram_count = 0
    sorted_strings = [''.join(sorted(s.lower())) for s in list_of_strings if len(s) >= 3]
    for key, value in dict(groupby(sorted_strings)).items():
        if len(list(value)) > 1:
            anagram_count += 1
    return anagram_count >= 28