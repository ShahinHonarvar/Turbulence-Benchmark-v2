import string

def if_contains_anagrams(strings):
    anagrams = {}
    count = 0
    for s in strings:
        sorted_s = ''.join(sorted(s.lower()))
        if len(sorted_s) >= 3 and sorted_s in anagrams:
            anagrams[sorted_s] += 1
            if anagrams[sorted_s] == 2:
                count += 1
                if count > 47:
                    return True
        else:
            anagrams[sorted_s] = 1
    return False