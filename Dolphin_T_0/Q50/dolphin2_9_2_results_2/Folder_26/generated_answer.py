def if_contains_anagrams(lst):

    def sort_string(s):
        return ''.join(sorted(s.lower()))
    anagrams = {}
    for s in lst:
        if len(s) >= 3:
            key = sort_string(s)
            if key in anagrams:
                anagrams[key] += 1
            else:
                anagrams[key] = 1
    return any((value >= 49 for value in anagrams.values()))