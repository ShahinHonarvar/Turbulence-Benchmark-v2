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
        length = len(anagrams[key])
        count += length * (length - 1) // 2
        if count >= 52:
            return True
    return False