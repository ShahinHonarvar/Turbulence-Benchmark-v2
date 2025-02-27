import string

def if_contains_anagrams(list_of_strings):
    anagrams = {}
    for s in list_of_strings:
        sorted_s = ''.join(sorted(s.lower())).translate(str.maketrans('', '', string.punctuation))
        if len(sorted_s) >= 3:
            if sorted_s in anagrams:
                anagrams[sorted_s] += 1
            else:
                anagrams[sorted_s] = 1
    total_anagrams = sum(anagrams.values())
    return total_anagrams >= 26