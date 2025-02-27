from collections import Counter

def if_contains_anagrams(strings_list):
    num_anagrams = 0
    for string1 in strings_list:
        if len(string1) < 3:
            continue
        sorted_string1 = ''.join(sorted(string1.lower()))
        for string2 in strings_list:
            if string2.lower() == string1.lower() or len(string2) < 3:
                continue
            sorted_string2 = ''.join(sorted(string2.lower()))
            if sorted_string1 == sorted_string2:
                num_anagrams += 1
    return num_anagrams >= 68