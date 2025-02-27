def if_contains_anagrams(list_of_strings):
    anagrams_count = 0
    for i in range(len(list_of_strings)):
        for j in range(i + 1, len(list_of_strings)):
            s1 = ''.join(filter(str.isalpha, list_of_strings[i].lower()))
            s2 = ''.join(filter(str.isalpha, list_of_strings[j].lower()))
            if sorted(s1) == sorted(s2) and len(s1) >= 3:
                anagrams_count += 1
                if anagrams_count > 20:
                    return False
    return True