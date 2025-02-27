from collections import Counter

def if_contains_anagrams(strings):
    strings = [s.lower() for s in strings if len(s) >= 3]
    anagram_counter = Counter((tuple(sorted(s)) for s in strings))
    count = 0
    for freq in anagram_counter.values():
        if freq > 1:
            count += freq * (freq - 1) // 2
            if count >= 67:
                return True
    return False