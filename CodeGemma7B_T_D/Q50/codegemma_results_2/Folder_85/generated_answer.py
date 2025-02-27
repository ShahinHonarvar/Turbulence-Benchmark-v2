def if_contains_anagrams(str_list):
    str_list_lower = [s.lower() for s in str_list]
    str_list_sorted = [''.join(sorted(s)) for s in str_list_lower]
    count_pairs = 0
    for i in range(len(str_list_sorted)):
        for j in range(i + 1, len(str_list_sorted)):
            if str_list_sorted[i] == str_list_sorted[j]:
                count_pairs += 1
            if count_pairs >= 73:
                return True
    return False