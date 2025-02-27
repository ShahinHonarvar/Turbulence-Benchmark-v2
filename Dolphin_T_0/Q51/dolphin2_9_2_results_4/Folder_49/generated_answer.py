def if_contains_anagrams(list_of_strings):
    anagrams_count = 0
    for i in range(len(list_of_strings)):
        for j in range(i + 1, len(list_of_strings)):
            string1 = list_of_strings[i].lower()
            string2 = list_of_strings[j].lower()
            if len(string1) < 3 or len(string2) < 3 or sorted(string1) != sorted(string2):
                continue
            anagrams_count += 1
            if anagrams_count > 10:
                return False
    return True