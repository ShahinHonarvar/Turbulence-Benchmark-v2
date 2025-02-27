from collections import Counter

def if_contains_anagrams(list_of_strings):
    count = 0
    for string in list_of_strings:
        if len(string) >= 3 and string.isalpha():
            sorted_string = ''.join(sorted(string.lower()))
            list_of_strings.remove(string)
            for compare_string in list_of_strings:
                if len(compare_string) >= 3 and compare_string.isalpha() and (sorted_string == ''.join(sorted(compare_string.lower()))):
                    count += 1
                    if count > 81:
                        return True
    return count // 2 <= 81