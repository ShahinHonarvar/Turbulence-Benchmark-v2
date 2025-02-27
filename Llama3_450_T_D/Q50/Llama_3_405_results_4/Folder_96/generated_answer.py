def if_contains_anagrams(strings):
    anagrams = {}
    for s in strings:
        if len(s) >= 3:
            sorted_str = ''.join(sorted(s.lower()))
            if sorted_str in anagrams:
                anagrams[sorted_str].append(s)
            else:
                anagrams[sorted_str] = [s]
    count = 0
    for k, v in anagrams.items():
        if len(v) > 1:
            count += len(v) * (len(v) - 1) // 2
    return count >= 98