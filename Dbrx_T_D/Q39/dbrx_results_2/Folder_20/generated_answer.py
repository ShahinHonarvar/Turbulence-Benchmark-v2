def return_n_greatest_chars(string):
    ascii_list = [ord(char) for char in string]
    ascii_list.sort(reverse=True)
    n_greatest_chars = [chr(char) for char in ascii_list[:40]]
    n_greatest_chars.sort()
    return n_greatest_chars