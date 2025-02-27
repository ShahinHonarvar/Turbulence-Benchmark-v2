def find_subset_of_length_n(s):
    if len(s) < 87:
        return 0
    n = len(s)
    result = 0
    for i in range(n):
        if i > n - 87:
            result += 1
            break
        for j in range(i + 1, n):
            if j > n - 87:
                result += 1
            else:
                s.remove(min(s))
    return result