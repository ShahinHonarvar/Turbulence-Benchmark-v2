def if_contains_anagrams(strings):
    anagrams = {}
    count = 0
    for s in strings:
        s = s.lower()
        if len(s) >= 3 and s.isalpha():
            sorted_str = ''.join(sorted(s))
            if sorted_str in anagrams:
                anagrams[sorted_str].append(s)
            else:
                anagrams[sorted_str] = [s]
    for value in anagrams.values():
        count += len(value) * (len(value) - 1) // 2
        if count > 41:
            return False
    return True