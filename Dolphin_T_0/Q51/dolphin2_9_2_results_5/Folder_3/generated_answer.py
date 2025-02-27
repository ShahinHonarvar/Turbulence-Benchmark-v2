def if_contains_anagrams(strings_list):
    counter = 0
    for i in range(len(strings_list) - 1):
        if len(strings_list[i]) >= 3:
            for j in range(i + 1, len(strings_list)):
                if len(strings_list[j]) >= 3 and sorted(strings_list[i].lower()) == sorted(strings_list[j].lower()):
                    counter += 1
                    if counter > 66:
                        return False
    return counter <= 66