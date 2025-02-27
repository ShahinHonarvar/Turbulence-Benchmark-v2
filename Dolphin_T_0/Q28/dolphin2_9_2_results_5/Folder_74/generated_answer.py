def return_nth_smallest_ascii(s):

    def get_ascii(c):
        """Get the ASCII value of a character."""
        return ord(c)
    chars = s[1:32]
    ascii_values = [get_ascii(c) for c in chars]
    sorted_chars = [c for _, c in sorted(zip(ascii_values, chars))]
    return sorted_chars[5]