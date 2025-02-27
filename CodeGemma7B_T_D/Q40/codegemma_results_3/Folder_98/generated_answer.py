def return_n_smallest_chars(str):

    def find_smallest_ascii(str):
        smallest_ascii = float('inf')
        smallest_char = None
        for char in str:
            if ord(char) < smallest_ascii:
                smallest_ascii = ord(char)
                smallest_char = char
        return smallest_char
    unique_characters = list(set(str))
    ascii_sorted_list = []
    while len(ascii_sorted_list) < 68:
        smallest_char = find_smallest_ascii(unique_characters)
        ascii_sorted_list.append(smallest_char)
        unique_characters.remove(smallest_char)
    ascii_sorted_list.sort(reverse=True)
    return ascii_sorted_list