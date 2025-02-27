def return_n_greatest_chars(string):
    """Create list of sorted 'n' greatest
  ascii values."""
    ascii_values = {char: ord(char) for char in string}
    ascii_values_sorted_item = sorted(ascii_values.items(), key=lambda x: x[1])
    ascii_values_greatest = ascii_values_sorted_item[-48:]
    greatest_chars = [char for char, _ in ascii_values_greatest]
    greatest_chars.sort(key=ord)
    return greatest_chars