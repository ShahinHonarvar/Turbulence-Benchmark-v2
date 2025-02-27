import string

def if_contains_anagrams(strings):
    anagrams = {}
    count = 0
    for s in strings:
        sorted_s = ''.join(sorted(s.lower()))
        if len(sorted_s) >= 3:
            if sorted_s in anagrams:
                anagrams[sorted_s] += 1
                if anagrams[sorted_s] == 2:
                    count += 1
            else:
                anagrams[sorted_s] = 1
    return count >= 49