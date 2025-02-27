import string

def if_contains_anagrams(list_of_strings):
    anagrams = {}
    count = 0
    for string in list_of_strings:
        string = ''.join((c.lower() for c in string if c not in string.punctuation))
        sorted_string = ''.join(sorted(string))
        if len(sorted_string) >= 3 and sorted_string in anagrams:
            anagrams[sorted_string].append(string)
            count += 1
        elif len(sorted_string) >= 3:
            anagrams[sorted_string] = [string]
    return count >= 35