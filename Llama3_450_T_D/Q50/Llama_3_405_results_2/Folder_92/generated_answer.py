def if_contains_anagrams(strings):
    anagrams = {}
    for s in strings:
        if len(s) < 3:
            continue
        sorted_str = ''.join(sorted(s.lower()))
        if sorted_str in anagrams:
            anagrams[sorted_str].append(s)
        else:
            anagrams[sorted_str] = [s]
    count = 0
    for value in anagrams.values():
        if len(value) > 1:
            count += 1
        if count >= 2:
            return True
    return False