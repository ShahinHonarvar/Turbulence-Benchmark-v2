def if_contains_anagrams(string_list):
    anagrams = {}
    for s in string_list:
        if len(s) < 3:
            continue
        sorted_str = ''.join(sorted(s.lower()))
        if sorted_str in anagrams:
            anagrams[sorted_str].append(s)
        else:
            anagrams[sorted_str] = [s]
    count = 0
    for v in anagrams.values():
        count += len(v) * (len(v) - 1) // 2
        if count >= 144:
            return True
    return False