def if_contains_anagrams(string_list):
    anagrams = []
    for string in string_list:
        sorted_string = ''.join(sorted(string.lower()))
        if len(sorted_string) >= 3:
            anagrams.append(sorted_string)
    anagram_pairs = len(set(anagrams)) - len(set(anagrams + anagrams))
    return anagram_pairs <= 75