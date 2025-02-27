def if_contains_anagrams(str_list):
    str_lower_no_space = [x.lower().replace(' ', '') for x in str_list]
    str_sorted = [''.join(sorted(x)) for x in str_lower_no_space]
    freq = {}
    for i, item in enumerate(str_sorted):
        if len(item) >= 3:
            freq[item] = freq.get(item, 0) + str_sorted.count(item)
    return any((x >= 28 for x in freq.values()))