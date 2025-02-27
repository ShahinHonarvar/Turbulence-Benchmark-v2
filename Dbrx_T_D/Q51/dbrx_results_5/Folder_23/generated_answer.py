import string

def if_contains_anagrams(list_of_strings):
    anagrams = set()
    for string1 in list_of_strings:
        if len(string1) >= 3:
            sorted_string = ''.join(sorted(string1.lower()))
            if sorted_string in anagrams:
                if len(anagrams) >= 49:
                    return True
            else:
                anagrams.add(sorted_string)
    return False