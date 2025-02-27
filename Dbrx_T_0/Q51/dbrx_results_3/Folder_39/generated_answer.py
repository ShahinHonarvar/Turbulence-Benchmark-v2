import string

def if_contains_anagrams(strings):
    anagrams = {}
    for s in strings:
        s = s.lower()
        if len(s) < 3 or not s.isalpha():
            continue
        sorted_s = ''.join(sorted(s))
        if sorted_s in anagrams:
            anagrams[sorted_s] += 1
            if anagrams[sorted_s] > 257:
                return False
        else:
            anagrams[sorted_s] = 1
    return True