def if_contains_anagrams(list_of_strings):
    anagrams = {}
    for s in list_of_strings:
        sorted_s = ''.join(sorted(s.lower()))
        if sorted_s in anagrams:
            anagrams[sorted_s] += 1
        else:
            anagrams[sorted_s] = 1
    for count in anagrams.values():
        if count > 1 and len(anagrams) >= 3:
            return True
    return False