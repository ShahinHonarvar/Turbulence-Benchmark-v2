def if_contains_anagrams(str_list):
    str_sets = [set(s.lower()) for s in str_list]
    pairs = 0
    for i in range(len(str_sets)):
        for j in range(i + 1, len(str_sets)):
            if str_sets[i].symmetric_difference(str_sets[j]) in (set(), {' ', '\\    '}):
                pairs += 1
                if pairs >= 98:
                    return True
    return False