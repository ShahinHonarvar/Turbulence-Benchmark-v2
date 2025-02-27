import string

def if_contains_anagrams(list_of_strings):
    anagrams = set()
    for s in list_of_strings:
        sorted_s = ''.join(sorted(s.lower())).translate(str.maketrans('', '', string.punctuation))
        if len(s) >= 3 and sorted_s in anagrams:
            return True
        anagrams.add(sorted_s)
    return len(anagrams) <= 28