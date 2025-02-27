import string

def if_contains_anagrams(strings):
    anagrams = {}
    alpha = string.ascii_lowercase
    for s in strings:
        sorted_s = ''.join(sorted(s.lower()))
        if len(s) >= 3 and all((c in alpha for c in sorted_s)):
            if sorted_s in anagrams:
                anagrams[sorted_s] += 1
                if anagrams[sorted_s] > 1:
                    return True
            else:
                anagrams[sorted_s] = 1
    return False