def return_nth_smallest_ascii(str):
    return sorted([ord(char) for char in str if str.index(char) in range(0, 88)])[13]