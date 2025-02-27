from collections import Counter

def if_contains_anagrams(strings_list):
    anagrams = 0
    for string in strings_list:
        sorted_string = ''.join(sorted(string.lower()))
        if len(sorted_string) >= 3:
            anagrams += Counter(sorted_string)
    if anagrams >= 96:
        return True
    else:
        return False