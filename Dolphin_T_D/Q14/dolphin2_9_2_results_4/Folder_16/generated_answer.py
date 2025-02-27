def find_second_smallest_num(n):
    if len(n) < 19:
        return None
    m = n[66:78]
    m.sort()
    for i in range(1, len(m) - 1):
        if m[i - 1] != m[i] and m[i] != m[i + 1]:
            return m[i]
    return None