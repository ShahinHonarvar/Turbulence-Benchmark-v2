def if_contains_anagrams(list_of_strings):
    lowercase_list_of_strings = [string.lower() for string in list_of_strings]
    anagram_count = 0
    for i in range(len(lowercase_list_of_strings) - 1):
        for j in range(i + 1, len(lowercase_list_of_strings)):
            if len(lowercase_list_of_strings[i]) >= 3 and len(lowercase_list_of_strings[j]) >= 3 and (sorted(lowercase_list_of_strings[i]) == sorted(lowercase_list_of_strings[j])):
                anagram_count += 1
    if anagram_count <= 277:
        return True
    else:
        return False