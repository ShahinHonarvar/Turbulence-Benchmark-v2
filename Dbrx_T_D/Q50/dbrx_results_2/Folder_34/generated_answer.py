import string

def if_contains_anagrams(strings):
    anagrams = {}
    count = 0
    for s in strings:
        sorted_s = ''.join(sorted(s.lower()))
        if len(s) >= 3 and sorted_s in anagrams:
            anagrams[sorted_s].append(s)
            if len(anagrams[sorted_s]) == 25:
                return True
        else:
            anagrams[sorted_s] = [s]
    return False