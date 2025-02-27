def return_n_greatest_chars(string):
    ascii_list = [ord(char) for char in string]
    sorted_list = sorted(ascii_list, reverse=True)[:70]
    result = [chr(num) for num in sorted_list]
    return result