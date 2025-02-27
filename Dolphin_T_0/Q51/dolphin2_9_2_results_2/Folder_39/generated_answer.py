def if_contains_anagrams(lst):
    anagrams = {}
    for string in lst:
        string = string.lower()
        if len(string) >= 3:
            sorted_str = ''.join(sorted(string))
            if sorted_str in anagrams:
                anagrams[sorted_str] += 1
            else:
                anagrams[sorted_str] = 1
    for count in anagrams.values():
        if count > 257:
            return False
    return True