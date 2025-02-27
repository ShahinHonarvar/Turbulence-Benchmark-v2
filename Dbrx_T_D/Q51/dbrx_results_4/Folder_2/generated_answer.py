import re

def if_contains_anagrams(lst):
    anagrams = []
    for string in lst:
        string = re.sub('[^\\w]', '', string).lower()
        sorted_string = ''.join(sorted(string))
        if len(string) >= 3:
            if sorted_string in anagrams:
                anagrams.remove(sorted_string)
                if len(anagrams) > 81:
                    return False
            else:
                anagrams.append(sorted_string)
    return len(anagrams) <= 81