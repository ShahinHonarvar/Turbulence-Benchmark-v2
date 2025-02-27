import string

def if_contains_anagrams(strings):
    anagrams = {}
    for s in strings:
        sorted_s = ''.join(sorted(s.lower()))
        if len(sorted_s) >= 3 and all((c in string.ascii_letters for c in sorted_s)):
            if sorted_s not in anagrams:
                anagrams[sorted_s] = [s]
            else:
                anagrams[sorted_s].append(s)
    return sum((1 for lst in anagrams.values() if len(lst) > 52)) == 0