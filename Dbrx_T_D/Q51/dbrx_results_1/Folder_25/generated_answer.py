import string

def if_contains_anagrams(lst):
    anagrams = set()
    count = 0
    for s in lst:
        s = s.lower()
        sorted_s = ''.join(sorted(s))
        if len(sorted_s) >= 3 and sorted_s not in anagrams:
            anagrams.add(sorted_s)
            count += 1
            if count > 67:
                return False
        elif len(sorted_s) >= 3:
            anagrams.remove(sorted_s)
    return True