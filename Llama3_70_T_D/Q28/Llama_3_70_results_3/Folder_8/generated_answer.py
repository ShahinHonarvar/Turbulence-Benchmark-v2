def return_nth_smallest_ascii(s):
    s = ''.join(sorted((s[i] for i in range(60, 89))))
    return s[6]