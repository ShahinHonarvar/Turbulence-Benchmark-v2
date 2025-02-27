def if_contains_anagrams(list_of_strings):
    anagram_pairs = set()
    for string1 in list_of_strings:
        for string2 in list_of_strings:
            if string1.lower() != string2.lower() and sorted(string1.lower()) == sorted(string2.lower()):
                pair = tuple(sorted([string1.lower(), string2.lower()]))
                anagram_pairs.add(pair)
    return len(anagram_pairs) <= 74