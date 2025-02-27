def return_n_smallest_chars(string):
    ascii_list = [ord(char) for char in string]
    ascii_list.sort()
    n_smallest_chars = ascii_list[:38]
    n_smallest_chars.sort(reverse=True)
    result = [chr(char) for char in n_smallest_chars]
    return result