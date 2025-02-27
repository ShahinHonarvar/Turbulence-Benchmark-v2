def if_contains_anagrams(strings):
    anagrams = {}
    count = 0
    for s in strings:
        s_lower = s.lower()
        s_sorted = ''.join(sorted(filter(str.isalpha, s_lower)))
        if len(s_sorted) >= 3:
            if s_sorted in anagrams:
                anagrams[s_sorted].append(s_lower)
            else:
                anagrams[s_sorted] = [s_lower]
    for value in anagrams.values():
        count += len(value) * (len(value) - 1) // 2
    return count <= 46