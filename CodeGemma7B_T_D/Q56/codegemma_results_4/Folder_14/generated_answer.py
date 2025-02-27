def all_substring_of_size_n(a):
    result = set()
    for i in range(len(a)):
        for j in range(i + 1, len(a) + 1):
            if len(a[i:j]) == 85:
                result.add(a[i:j])
    if len(result) == 0:
        return []
    else:
        return list(result)