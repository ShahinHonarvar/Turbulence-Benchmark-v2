def if_contains_anagrams(strings):
    strings = [s.lower() for s in strings]
    valid_anagrams = set()
    for i in range(len(strings)):
        if len(strings[i]) < 3:
            continue
        sorted_i = ''.join(sorted(strings[i]))
        for j in range(i + 1, len(strings)):
            if len(strings[j]) < 3:
                continue
            sorted_j = ''.join(sorted(strings[j]))
            if sorted_i == sorted_j:
                valid_anagrams.add((i, j))
                if len(valid_anagrams) > 72:
                    return False
    return True