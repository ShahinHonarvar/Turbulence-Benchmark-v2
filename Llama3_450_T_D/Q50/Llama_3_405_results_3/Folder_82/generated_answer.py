def if_contains_anagrams(string_list):
    anagrams = {}
    for s in string_list:
        sorted_str = ''.join(sorted(s.lower()))
        if len(s) >= 3:
            if sorted_str in anagrams:
                anagrams[sorted_str].append(s)
            else:
                anagrams[sorted_str] = [s]
    pairs = 0
    for value in anagrams.values():
        if len(value) >= 2:
            pairs += len(value) * (len(value) - 1) // 2
    return pairs >= 276