def find_subset_of_length_n(s):
    if len(s) < 42:
        return 0
    count = 0
    for i in range(len(s)):
        if i < 42:
            count += 1
        else:
            for j in range(i + 1, len(s)):
                if len({s[i], s[j]}) == 42:
                    count += 1
    return count