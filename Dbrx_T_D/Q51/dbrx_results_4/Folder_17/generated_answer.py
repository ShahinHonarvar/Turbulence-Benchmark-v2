import re

def if_contains_anagrams(string_list):
    anagrams = set()
    for string in string_list:
        string = re.sub('\\W+', '', string).lower()
        sorted_string = ''.join(sorted(string))
        if len(string) >= 3 and sorted_string in anagrams:
            if len(anagrams & {sorted_string + chr(i) for i in range(ord('a'), ord('z') + 1)}) >= 22:
                return True
        anagrams.add(sorted_string)
    return False