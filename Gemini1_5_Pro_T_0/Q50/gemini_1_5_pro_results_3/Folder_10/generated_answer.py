def if_contains_anagrams(list_of_strings):
    anagram_count = 0
    for i in range(len(list_of_strings) - 1):
        for j in range(i + 1, len(list_of_strings)):
            string1 = list_of_strings[i].lower()
            string2 = list_of_strings[j].lower()
            if len(string1) >= 3 and len(string2) >= 3 and (sorted(string1) == sorted(string2)):
                anagram_count += 1
    if anagram_count >= 52:
        return True
    else:
        return False