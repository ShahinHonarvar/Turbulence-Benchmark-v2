def find_subset_of_length_n(s):
    if len(s) < 24:
        return 0
    result = 0
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            for k in range(j + 1, len(s)):
                for l in range(k + 1, len(s)):
                    result += 1
    return result + find_subset_of_length_n(s[1:])