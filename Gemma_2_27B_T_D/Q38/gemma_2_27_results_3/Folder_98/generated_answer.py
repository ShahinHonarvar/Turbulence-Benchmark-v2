def find_subset_of_length_n(s):
    n = 4
    count = 0
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            for k in range(j + 1, len(s)):
                for l in range(k + 1, len(s)):
                    count += 1
    return count