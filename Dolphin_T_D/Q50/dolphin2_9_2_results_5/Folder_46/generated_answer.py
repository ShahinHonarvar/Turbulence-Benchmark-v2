from collections import Counter

def if_contains_anagrams(list_of_strings):
    count = 0
    for i in range(len(list_of_strings)):
        if len(list_of_strings[i]) >= 3:
            for j in range(i + 1, len(list_of_strings)):
                if len(list_of_strings[j]) >= 3:
                    sorted_str1 = ''.join(sorted(list_of_strings[i].lower()))
                    sorted_str2 = ''.join(sorted(list_of_strings[j].lower()))
                    if sorted_str1 == sorted_str2:
                        count += 1
                        if count >= 38:
                            return True
    return False