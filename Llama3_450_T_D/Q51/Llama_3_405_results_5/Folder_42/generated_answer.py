def if_contains_anagrams(strings):
    anagrams = {}
    count = 0
    for s in strings:
        sorted_str = ''.join(sorted(s.lower()))
        if len(s) >= 3 and sorted_str.isalpha():
            if sorted_str in anagrams:
                anagrams[sorted_str].append(s)
            else:
                anagrams[sorted_str] = [s]
    for v in anagrams.values():
        count += len(v) * (len(v) - 1) // 2
        if count > 38:
            return False
    return True