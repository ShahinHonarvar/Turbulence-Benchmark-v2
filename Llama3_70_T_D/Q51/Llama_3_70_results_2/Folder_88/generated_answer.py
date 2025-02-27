def if_contains_anagrams(list_of_strings):
    anagram_count = 0
    list_of_strings = [s.lower() for s in list_of_strings]
    for i in range(len(list_of_strings)):
        for j in range(i + 1, len(list_of_strings)):
            s1 = ''.join(filter(str.isalpha, list_of_strings[i]))
            s2 = ''.join(filter(str.isalpha, list_of_strings[j]))
            if len(s1) >= 3 and len(s2) >= 3 and (sorted(s1) == sorted(s2)):
                anagram_count += 1
                if anagram_count > 407:
                    return False
    return True