def find_subset_of_length_n(s):
    n = 91
    count = 0
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            temp = set(list(s)[i:j])
            if len(temp) == n:
                count += 1
    return count