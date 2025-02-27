def find_subset_of_length_n(s):
    if len(s) < 99:
        return 0
    count = 0
    for i in range(len(s)):
        if i == 0 or s[i] != s[i - 1]:
            subset = {s[i]}
            for j in range(i + 1, len(s)):
                if s[j] not in subset:
                    subset.add(s[j])
                    if len(subset) == 99:
                        count += 1
    return count