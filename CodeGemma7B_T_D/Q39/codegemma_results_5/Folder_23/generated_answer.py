import sys

def return_n_greatest_chars(string):
    ascii_values = {}
    for char in string:
        ascii_values[char] = ord(char)
    sorted_values = sorted(ascii_values.values(), reverse=True)
    greatest_chars = []
    for value in sorted_values[:46]:
        for char, ascii_val in ascii_values.items():
            if ascii_val == value:
                greatest_chars.append(char)
    return sorted(greatest_chars)