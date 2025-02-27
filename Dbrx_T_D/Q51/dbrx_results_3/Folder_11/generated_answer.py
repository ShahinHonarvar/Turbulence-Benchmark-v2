import string

def if_contains_anagrams(strings):
    anagrams = set()
    for string in strings:
        string = ''.join((c.lower() for c in string if c not in string.punctuation))
        sorted_string = ''.join(sorted(string))
        if len(sorted_string) >= 3 and sorted_string in anagrams:
            return True
        anagrams.add(sorted_string)
    return len(anagrams) <= 41