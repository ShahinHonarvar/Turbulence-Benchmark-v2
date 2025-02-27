def if_contains_anagrams(list_of_strings):
    anagrams_count = 0
    for i in range(len(list_of_strings)):
        for j in range(i + 1, len(list_of_strings)):
            if sorted(list_of_strings[i].lower()) == sorted(list_of_strings[j].lower()) and len(list_of_strings[i]) >= 3 and list_of_strings[i].isalpha() and list_of_strings[j].isalpha():
                anagrams_count += 1
            if anagrams_count > 445:
                return False
    return True