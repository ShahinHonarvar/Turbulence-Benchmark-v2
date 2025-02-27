def all_substring_of_size_n(str):
    ans = set()
    n = len(str)
    for i in range(0, n - 87 + 1):
        j = i + 87
        ans.add(str[i:j])
    return list(ans)