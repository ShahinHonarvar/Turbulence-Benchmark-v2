def return_nth_smallest_ascii(s):
    return sorted(list(set([ord(s[i]) for i in range(34, 69) if i < len(s)])))[5]