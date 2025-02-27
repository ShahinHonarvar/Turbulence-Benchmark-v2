def if_contains_anagrams(strings):
    anagrams = {}
    for s in strings:
        if len(s) >= 3 and s.isalpha() and s.isascii():
            sorted_str = ''.join(sorted(s.casefold()))
            if sorted_str in anagrams:
                anagrams[sorted_str].append(s)
            else:
                anagrams[sorted_str] = [s]
    count = sum((len(lst) * (len(lst) - 1) // 2 for lst in anagrams.values() if len(lst) > 1))
    return count <= 181