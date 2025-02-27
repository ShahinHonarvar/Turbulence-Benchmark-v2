def return_nth_smallest_ascii(s):
    return sorted([ord(char) for char in s[3:53] if char not in s[3:53]])[7]