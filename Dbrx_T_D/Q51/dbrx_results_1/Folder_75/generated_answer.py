import string

def if_contains_anagrams(strings):
    anagrams = {}
    count = 0
    for s in strings:
        s = s.lower()
        s = ''.join((c for c in s if c in string.ascii_letters))
        sorted_s = ''.join(sorted(s))
        if len(s) < 3:
            continue
        if sorted_s in anagrams:
            anagrams[sorted_s] += 1
            if anagrams[sorted_s] == 2:
                count += 1
        else:
            anagrams[sorted_s] = 1
    return count <= 55