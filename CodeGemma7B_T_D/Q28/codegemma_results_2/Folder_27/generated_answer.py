from functools import partial

def return_nth_smallest_ascii(txt):

    def helper(x):
        ascii_values = {char: ord(char) for char in txt[33:86] if char == x}
        return ascii_values[x]
    nth_smallest = partial(min, key=helper)
    return nth_smallest(repeated_chars)