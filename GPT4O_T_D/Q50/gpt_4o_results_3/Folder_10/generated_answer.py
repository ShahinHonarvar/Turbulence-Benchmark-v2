def if_contains_anagrams(strings):
    a_dict = {}
    count = 0
    for s in strings:
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s.lower()))
            if sorted_s in a_dict:
                a_dict[sorted_s] += 1
            else:
                a_dict[sorted_s] = 1
    for v in a_dict.values():
        if v > 1:
            count += v * (v - 1) // 2
    return count >= 52