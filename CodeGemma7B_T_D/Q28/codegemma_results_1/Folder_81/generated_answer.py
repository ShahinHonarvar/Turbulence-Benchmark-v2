def return_nth_smallest_ascii(test_str):
    return sorted([ord(char) for char in test_str])[13]