import string

def if_contains_anagrams(strings):
    anagrams = {}
    for s in strings:
        sorted_s = ''.join(sorted(s.lower()))
        if len(sorted_s) >= 3:
            if sorted_s not in anagrams:
                anagrams[sorted_s] = 1
            else:
                anagrams[sorted_s] += 1
    total_anagrams = sum([v // 2 for v in anagrams.values()])
    return total_anagrams >= 47