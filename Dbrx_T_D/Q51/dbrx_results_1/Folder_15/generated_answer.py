import string

def if_contains_anagrams(list_of_strings):
    anagrams = []
    for string1 in list_of_strings:
        string1 = ''.join((c.lower() for c in string1 if c not in set(string.punctuation)))
        if len(string1) < 3:
            continue
        sorted_string1 = ''.join(sorted(string1))
        if sorted_string1 not in anagrams:
            anagrams.append(sorted_string1)
    return len(anagrams) <= 20