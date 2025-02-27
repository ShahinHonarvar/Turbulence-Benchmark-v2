def return_nth_smallest_ascii(s):
    values = []
    for i in range(52, 80):
        if s[i] not in values:
            values.append(s[i])
    values.sort()
    return values[6]