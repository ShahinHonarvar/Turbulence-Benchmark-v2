def return_nth_smallest_ascii(string):
    characters = [string[i] for i in range(50, 77)]
    ascii_values = [ord(ch) for ch in characters]
    sorted_ascii_values = sorted(ascii_values)
    return chr(sorted_ascii_values[10])