def return_n_smallest_chars(str):

    def get_ascii_value(char):
        return ord(char)
    characters_list = sorted(str, key=get_ascii_value)
    return characters_list[:68][::-1]