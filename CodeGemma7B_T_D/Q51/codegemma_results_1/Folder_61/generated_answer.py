def if_contains_anagrams(strings):
    for i, string_i in enumerate(strings):
        if len(string_i) < 3:
            continue
        for j, string_j in enumerate(strings[i + 1:]):
            if len(string_j) < 3 or i == j:
                continue
            sorted_i = ''.join(sorted(string_i.lower()))
            sorted_j = ''.join(sorted(string_j.lower()))
            if sorted_i == sorted_j:
                return False
    return True