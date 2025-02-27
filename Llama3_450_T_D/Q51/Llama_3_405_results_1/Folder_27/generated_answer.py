def if_contains_anagrams(strings):
    anagrams = {}
    for s in strings:
        s = ''.join(filter(str.isalpha, s)).lower()
        if len(s) >= 3:
            sorted_str = ''.join(sorted(s))
            if sorted_str in anagrams:
                anagrams[sorted_str].append(s)
            else:
                anagrams[sorted_str] = [s]
    count = 0
    for value in anagrams.values():
        count += len(value) * (len(value) - 1) // 2
        if count > 113:
            return False
    return True