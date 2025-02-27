def if_contains_anagrams(list_of_strings):
    anagrams_count = 0
    for i in range(len(list_of_strings)):
        for j in range(i + 1, len(list_of_strings)):
            if len(list_of_strings[i]) >= 3 and len(list_of_strings[j]) >= 3:
                list_of_strings[i] = ''.join(sorted(list_of_strings[i].lower()))
                list_of_strings[j] = ''.join(sorted(list_of_strings[j].lower()))
                if list_of_strings[i] == list_of_strings[j]:
                    anagrams_count += 1
    return anagrams_count <= 26