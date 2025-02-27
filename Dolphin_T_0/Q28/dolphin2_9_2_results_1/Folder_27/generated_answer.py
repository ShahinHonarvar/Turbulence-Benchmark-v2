def return_nth_smallest_ascii(s):
    filtered_s = [c for i, c in enumerate(s) if 33 <= i <= 85]
    filtered_s.sort(key=lambda c: ord(c))
    return filtered_s[12]