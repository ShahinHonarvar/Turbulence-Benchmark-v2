def if_contains_anagrams(strings):
    anagrams = {}
    count = 0
    for s in strings:
        s = s.lower()
        if len(s) < 3:
            continue
        sorted_str = ''.join(sorted(s))
        if sorted_str in anagrams:
            if len(anagrams[sorted_str]) == 1:
                count += 1
                if count > 9:
                    return False
            anagrams[sorted_str].append(s)
        else:
            anagrams[sorted_str] = [s]
    return True