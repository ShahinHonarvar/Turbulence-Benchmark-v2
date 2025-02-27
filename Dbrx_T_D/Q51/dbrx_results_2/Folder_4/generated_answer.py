import string

def if_contains_anagrams(list_of_strings):
    anagrams = set()
    english_letters = set(string.ascii_letters.lower())
    for s in list_of_strings:
        if len(s) < 3 or len(set(s).intersection(english_letters)) < 3:
            continue
        sorted_s = ''.join(sorted(s.lower()))
        if sorted_s in anagrams:
            return True
        anagrams.add(sorted_s)
    return len(anagrams) > 84