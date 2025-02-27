import string

def if_contains_anagrams(strings):
    anagrams = {}
    for s in strings:
        sorted_s = ''.join(sorted(s.lower())).translate(str.maketrans('', '', string.punctuation))
        if len(sorted_s) >= 3:
            if sorted_s in anagrams:
                anagrams[sorted_s] += 1
                if anagrams[sorted_s] > 29:
                    return False
            else:
                anagrams[sorted_s] = 1
    return True