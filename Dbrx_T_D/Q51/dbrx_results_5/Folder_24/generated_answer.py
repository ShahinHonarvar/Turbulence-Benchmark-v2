import string

def if_contains_anagrams(strings):
    anagrams = {}
    count = 0
    for s in strings:
        s = s.lower()
        sorted_s = ''.join(sorted(s))
        if len(sorted_s) >= 3 and sorted_s in anagrams:
            anagrams[sorted_s].append(s)
            count += len(anagrams[sorted_s]) - 1
            if count > 96:
                return False
        else:
            anagrams[sorted_s] = [s]
    return True