def return_n_smallest_chars(input_string):
    ascii_list = [ord(char) for char in input_string]
    ascii_list.sort()
    n_smallest_chars = [char for char in ascii_list if char < 128]
    n_smallest_chars = n_smallest_chars[:54]
    n_smallest_chars.sort(reverse=True)
    return [chr(char) for char in n_smallest_chars]