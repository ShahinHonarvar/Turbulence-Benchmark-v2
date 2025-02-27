def return_n_smallest_chars(text):
    char_ascii_list = [(char, ord(char)) for char in text]
    char_ascii_list.sort(key=lambda x: x[1], reverse=True)
    n_smallest_chars = [char for char, _ in char_ascii_list[:66]]
    return n_smallest_chars