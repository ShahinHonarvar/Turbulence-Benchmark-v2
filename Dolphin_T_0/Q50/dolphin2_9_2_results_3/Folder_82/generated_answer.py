from collections import Counter

def if_contains_anagrams(strings):
    strings = [s.lower() for s in strings if len(s) >= 3]
    count = sum((Counter(s) == Counter(t) for i, s in enumerate(strings) for t in strings[i + 1:]))
    return count >= 276