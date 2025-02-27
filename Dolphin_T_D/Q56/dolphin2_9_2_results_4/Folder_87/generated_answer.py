def all_substring_of_size_n(s):
    n = 58
    result = []
    for i in range(len(s)):
        for j in range(i + n, len(s) + 1):
            if len(set(s[i:j])) == n and len(s[i:j]) == n:
                result.append(s[i:j])
    unique_result = list(set(result))
    if len(unique_result) == 0:
        return []
    else:
        return unique_result