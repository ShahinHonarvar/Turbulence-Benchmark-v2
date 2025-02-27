def return_nth_smallest_ascii(s):
    return sorted([s[i] for i in range(50, 77) if s[i].isascii()])[10]