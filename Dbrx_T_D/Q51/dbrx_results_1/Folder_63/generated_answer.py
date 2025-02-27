import string

def if_contains_anagrams(string_list):
    anagrams = set()
    valid_letters = set(string.ascii_letters.lower())
    for s in string_list:
        sorted_s = ''.join(sorted((c.lower() for c in s if c.lower() in valid_letters)))
        if len(sorted_s) >= 3:
            anagrams.add(sorted_s)
    return len(anagrams) <= 423