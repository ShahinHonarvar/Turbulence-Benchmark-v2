def if_contains_anagrams(strings):
    anagrams = {}
    count = 0
    for s in strings:
        if len(s) >= 3:
            sorted_str = ''.join(sorted(s.lower()))
            if sorted_str in anagrams:
                anagrams[sorted_str].append(s)
            else:
                anagrams[sorted_str] = [s]
    for key in anagrams:
        if len(anagrams[key]) > 1:
            count += len(anagrams[key]) * (len(anagrams[key]) - 1) // 2
    return count >= 314