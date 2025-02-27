def return_nth_smallest_ascii(word):
    word = word[34:69]
    ascii_values = [ord(char) for char in word]
    ascii_values.sort()
    return chr(ascii_values[5])