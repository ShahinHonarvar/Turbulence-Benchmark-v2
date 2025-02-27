def return_nth_smallest_ascii(s):
    for i in range(36, 80):
        for c in s[i:]:
            if ord(c) < ord(result):
                result = c
    return result