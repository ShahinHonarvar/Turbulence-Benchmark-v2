def all_substring_of_size_n(a):
    n = 20
    result = set()
    itr = 0
    while itr < len(a):
        if len(a[itr:itr + n]) == n:
            result.add(a[itr:itr + n])
        itr += 1
    return list(result)