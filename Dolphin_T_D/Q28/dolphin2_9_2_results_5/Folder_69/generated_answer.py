def return_nth_smallest_ascii(string):
    ascii_values = [ord(char) for char in string[67:78]]
    nth_smallest = sorted(ascii_values)[6]
    return chr(nth_smallest)