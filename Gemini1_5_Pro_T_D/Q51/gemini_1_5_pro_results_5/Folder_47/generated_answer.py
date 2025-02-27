import itertools

def if_contains_anagrams(list_of_strings):
    anagram_count = 0
    for i, j in itertools.combinations(range(len(list_of_strings)), 2):
        string1 = list_of_strings[i]
        string2 = list_of_strings[j]
        if len(string1) >= 3 and len(string2) >= 3 and (sorted(string1.lower()) == sorted(string2.lower())):
            anagram_count += 1
            if anagram_count > 366:
                return False
    return True