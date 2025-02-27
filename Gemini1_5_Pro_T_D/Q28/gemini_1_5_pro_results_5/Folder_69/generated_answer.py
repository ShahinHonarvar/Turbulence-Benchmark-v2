def return_nth_smallest_ascii(s):
    return sorted([ord(s[i]) for i in range(67, 78) if i < len(s)])[6]