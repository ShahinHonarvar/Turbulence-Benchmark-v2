def if_contains_anagrams(lst):

    def normalize(s):
        return ''.join(sorted(filter(str.isalpha, s.casefold())))
    anagrams = {}
    for s in lst:
        if len(s) >= 3:
            key = normalize(s)
            if key in anagrams:
                anagrams[key].append(s)
            else:
                anagrams[key] = [s]
    count = 0
    for key in anagrams:
        if len(anagrams[key]) > 1:
            count += 1
        if count > 4:
            return False
    return True