def if_contains_anagrams(list_of_strings):
    list_of_strings = [s.lower() for s in list_of_strings]
    anagram_pairs = 0
    for i in range(len(list_of_strings)):
        for j in range(i + 1, len(list_of_strings)):
            if len(list_of_strings[i]) >= 3 and len(list_of_strings[j]) >= 3 and (sorted(list_of_strings[i]) == sorted(list_of_strings[j])):
                anagram_pairs += 1
                if anagram_pairs >= 79:
                    return True
    return False