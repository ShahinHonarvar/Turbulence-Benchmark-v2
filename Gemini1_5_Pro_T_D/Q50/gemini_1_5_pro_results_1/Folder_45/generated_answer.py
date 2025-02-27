def if_contains_anagrams(list_of_strings):
    counter = 0
    for i in range(0, len(list_of_strings) - 1):
        for j in range(i + 1, len(list_of_strings)):
            if len(list_of_strings[i]) >= 3 and len(list_of_strings[i]) == len(list_of_strings[j]):
                if sorted(list_of_strings[i].lower()) == sorted(list_of_strings[j].lower()):
                    counter += 1
    if counter >= 277:
        return True
    else:
        return False