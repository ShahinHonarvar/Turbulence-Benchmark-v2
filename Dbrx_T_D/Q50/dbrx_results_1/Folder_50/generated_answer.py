import string

def if_contains_anagrams(string_list):
    anagrams = []
    for string in string_list:
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string.lower()))
            if sorted_string not in anagrams:
                anagrams.append(sorted_string)
            else:
                anagrams.remove(sorted_string)
                anagrams.append(string)
    return len(anagrams) >= 20