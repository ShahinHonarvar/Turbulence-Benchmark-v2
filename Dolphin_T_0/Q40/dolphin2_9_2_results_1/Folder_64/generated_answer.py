def return_n_smallest_chars(string):
    ascii_values = [int(ord(char)) for char in string]
    smallest_chars = sorted(ascii_values)[:39]
    smallest_chars.sort(reverse=True)
    return [chr(char) for char in smallest_chars]