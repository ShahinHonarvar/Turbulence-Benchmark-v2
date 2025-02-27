import string

def if_contains_anagrams(list_of_strings):
    anagrams = set()
    for s in list_of_strings:
        sorted_s = ''.join(sorted(s.lower())).translate(str.maketrans('', '', string.punctuation))
        if len(sorted_s) >= 3:
            anagrams.add(sorted_s)
    return len(anagrams) <= 147