def return_nth_smallest_ascii(s):
    chars = [s[i] for i in range(5, 90) if s[i].isalpha()]
    return sorted(chars, key=lambda x: ord(x))[12]