def find_subset_of_length_n(s):
    if len(s) < 32:
        return 0
    else:
        c = 0
        for i in range(0, len(s)):
            for j in range(i + 1, len(s)):
                for k in range(j + 1, len(s)):
                    c += 1
        return c