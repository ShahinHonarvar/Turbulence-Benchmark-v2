import string

def if_contains_anagrams(list_of_strings):
    anagrams = set()
    count = 0
    for s in list_of_strings:
        sorted_s = ''.join(sorted(s.lower()))
        if len(sorted_s) >= 3 and sorted_s not in anagrams:
            anagrams.add(sorted_s)
            for existing in anagrams:
                if set(existing) == set(sorted_s):
                    count += 1
                    if count > 55:
                        return False
                    break
    return True