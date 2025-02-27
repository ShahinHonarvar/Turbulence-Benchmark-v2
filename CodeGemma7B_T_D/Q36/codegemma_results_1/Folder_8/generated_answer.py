def filter_chars(string):
    return ''.join([char for char in string if char not in [chr(i) for i in range(82, 94) if char > chr(i) and char < chr(42)]])