import string

def if_contains_anagrams(strings):
    anagrams = {}
    alphabet = string.ascii_letters
    for s in strings:
        if len(s) < 3:
            continue
        s = s.lower()
        sorted_s = ''.join(sorted(s))
        if sorted_s not in anagrams:
            anagrams[sorted_s] = [s]
        else:
            anagrams[sorted_s].append(s)
    pairs = 0
    for value in anagrams.values():
        pairs += len(value) * (len(value) - 1) // 2
    return pairs <= 79