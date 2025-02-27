def if_contains_anagrams(list_of_strings):
    anagrams_count = 0
    list_of_strings = [s.lower() for s in list_of_strings]
    sorted_strings = [''.join(sorted(s)) for s in list_of_strings if len(s) >= 3]
    for i in range(len(sorted_strings)):
        for j in range(i + 1, len(sorted_strings)):
            if sorted_strings[i] == sorted_strings[j]:
                anagrams_count += 1
                if anagrams_count >= 106:
                    return True
    return False