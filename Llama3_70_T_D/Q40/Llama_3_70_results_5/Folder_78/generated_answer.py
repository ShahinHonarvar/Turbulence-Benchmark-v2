def return_n_smallest_chars(string):
    ascii_values = [ord(char) for char in string]
    smallest_ascii = sorted(ascii_values)[:43]
    smallest_chars = [chr(i) for i in smallest_ascii]
    smallest_chars.sort(reverse=True)
    return smallest_chars