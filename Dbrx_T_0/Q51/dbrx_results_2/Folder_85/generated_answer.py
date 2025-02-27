import string

def if_contains_anagrams(strings):
    anagrams = {}
    for s in strings:
        sorted_s = ''.join(sorted(s.lower())).encode('utf-8')
        if len(s) >= 3 and sorted_s in anagrams:
            anagrams[sorted_s] += 1
            if anagrams[sorted_s] > 276:
                return False
        else:
            anagrams[sorted_s] = 1
    return True