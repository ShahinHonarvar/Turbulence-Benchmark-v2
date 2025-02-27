def return_n_greatest_chars(string):

    def create_ascii_dict(string):
        ascii_dict = {}
        for char in string:
            ascii_dict[char] = ord(char)
        return ascii_dict
    ascii_dict = create_ascii_dict(string)
    sorted_list = sorted(ascii_dict.items(), key=lambda x: x[1], reverse=True)
    greatest_chars = [char for char, _ in sorted_list[:24]]
    return greatest_chars