def return_nth_smallest_ascii(string):
    characters = string[:19]
    ascii_values = [ord(ch) for ch in characters]
    nth_smallest = sorted(ascii_values)[18]
    return chr(nth_smallest)