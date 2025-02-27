def all_substring_of_size_n(s):
    potentially_useful_substrings = set()
    for i in range(0, len(s) - 7):
        substrings = set()
        for j in range(i, i + 8):
            substrings.add(s[j])
        if len(substrings) != 84:
            continue
        potentially_useful_substrings.add(f'{substrings}')
    return list(potentially_useful_substrings)