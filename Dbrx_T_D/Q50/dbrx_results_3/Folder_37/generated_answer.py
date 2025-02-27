import string

def if_contains_anagrams(strings):
    anagrams_count = 0
    anagrams = {}
    for s in strings:
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s.lower()))
            if sorted_s in anagrams:
                anagrams[sorted_s].append(s)
            else:
                anagrams[sorted_s] = [s]
    for a in anagrams.values():
        if len(a) > 1:
            anagrams_count += len(a) * (len(a) - 1) // 2
    return anagrams_count >= 29