def return_nth_smallest_ascii(s):
    return sorted(list(set([ord(s[i]) for i in range(33, 61) if i < len(s)])))[17]