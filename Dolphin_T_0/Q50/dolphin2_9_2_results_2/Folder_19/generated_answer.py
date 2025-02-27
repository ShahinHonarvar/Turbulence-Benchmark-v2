def if_contains_anagrams(list_of_strings):
    anagrams_count = len([(s1, s2) for i, s1 in enumerate(list_of_strings) for s2 in list_of_strings[i + 1:] if len(s1) >= 3 and len(s2) >= 3 and (sorted(s1.lower()) == sorted(s2.lower())) and (s1 != s2)])
    return anagrams_count >= 84