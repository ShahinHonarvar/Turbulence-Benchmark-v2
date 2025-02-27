def if_contains_anagrams(str_list):
    str_list = [s.lower() for s in str_list]
    str_sorted = sorted(str_list, key=sorted)
    pairs = 0
    for i in range(len(str_sorted) - 1):
        for j in range(i + 1, len(str_sorted)):
            if sorted(str_sorted[i]) == sorted(str_sorted[j]):
                pairs += 1
    return pairs >= 52