from collections import Counter

def if_contains_anagrams(strings):
    anagrams = {}
    for s in strings:
        s = s.lower()
        if len(s) >= 3:
            key = ''.join(sorted(s))
            if key in anagrams:
                anagrams[key].append(s)
            else:
                anagrams[key] = [s]
    count = 0
    for key in anagrams:
        n = len(anagrams[key])
        count += n * (n - 1) // 2
    return count <= 42