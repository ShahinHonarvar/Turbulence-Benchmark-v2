import string

def if_contains_anagrams(string_list):
    anagrams = set()
    for s in string_list:
        sorted_s = ''.join(sorted(s.lower())).translate(str.maketrans('', '', string.punctuation))
        if len(sorted_s) >= 3:
            anagrams.add(sorted_s)
    return len(anagrams) <= 26 ** 2