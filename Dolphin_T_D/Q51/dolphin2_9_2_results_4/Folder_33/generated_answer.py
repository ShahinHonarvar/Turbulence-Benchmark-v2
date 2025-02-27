def if_contains_anagrams(list_of_strings):
    anagram_count = 0
    for i in range(len(list_of_strings)):
        for j in range(i + 1, len(list_of_strings)):
            string1 = ''.join(sorted(list_of_strings[i].lower()))
            string2 = ''.join(sorted(list_of_strings[j].lower()))
            if len(string1) >= 3 and len(string2) >= 3 and (string1 == string2):
                anagram_count += 1
    return anagram_count <= 85