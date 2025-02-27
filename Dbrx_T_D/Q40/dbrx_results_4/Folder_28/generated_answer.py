def return_n_smallest_chars(string):
    char_list = [ord(char) for char in string]
    sorted_list = sorted(char_list)[:3]
    sorted_chars = [chr(char) for char in sorted_list]
    return sorted_chars