def find_subset_of_length_n(s):
    n = 180
    count = 0
    for i in range(len(s)):
        for j in range(i, len(s)):
            if len(set(s[i:j + 1])) == n:
                count += 1
    return count