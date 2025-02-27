def find_subset_of_length_n(s, n):
    if not s:
        return 0
    count = 0
    for i in range(len(s)):
        for subset in find_subset_of_length_n(s - {s[i]}, n - 1):
            count += 1
    return count