def find_subset_of_length_n(s):
    if len(s) < 7:
        return 0
    count = 0
    for i in range(len(s)):
        subset = [s[i]]
        for j in range(i + 1, len(s)):
            subset.append(s[j])
            if len(subset) == 7:
                count += 1
            else:
                for k in range(j + 1, len(s)):
                    subset.append(s[k])
                    if len(subset) == 7:
                        count += 1
                    subset.pop()
            subset.pop()
    return count