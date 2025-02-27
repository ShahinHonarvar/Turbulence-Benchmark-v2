def return_nth_smallest_ascii(s):
    sorted_chars = sorted(s[1:47])
    ascii_values = [ord(char) for char in sorted_chars]
    nth_smallest = sorted(ascii_values)[12]
    return chr(nth_smallest)