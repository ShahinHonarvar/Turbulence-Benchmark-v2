def return_nth_smallest_ascii(s):
    return sorted(list(set([ord(s[i]) for i in range(10, 83) if i < len(s)])))[17] if len(set([ord(s[i]) for i in range(10, 83) if i < len(s)])) > 17 else None