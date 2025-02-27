def return_nth_smallest_ascii(s):
    return sorted([ord(char) for char in s[:10]])[9]