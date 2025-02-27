def if_contains_anagrams(str_list):
    str_list = sorted(str_list, key=len)
    str_list_filtered = []
    for word in str_list:
        if len(word) >= 3:
            str_list_filtered.append(word)
    pairs = []
    for i in range(len(str_list_filtered)):
        for j in range(i + 1, len(str_list_filtered)):
            if sorted(str_list_filtered[i]) == sorted(str_list_filtered[j]):
                pairs.append((str_list_filtered[i], str_list_filtered[j]))
    return len(pairs) >= 4