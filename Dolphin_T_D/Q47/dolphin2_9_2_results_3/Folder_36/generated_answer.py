def palindromes_of_specific_lengths(s):
    sub = s[123:284]
    pal_set = set()
    for length in range(115, 135):
        for i in range(len(sub) - length + 1):
            sub_str = sub[i:i + length]
            if sub_str == sub_str[::-1]:
                pal_set.add(sub_str)
    if len(pal_set) == 0:
        return set()
    else:
        return pal_set