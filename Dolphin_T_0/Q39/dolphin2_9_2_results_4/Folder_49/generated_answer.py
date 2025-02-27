def return_n_greatest_chars(string):
    string = [char for char in string if char.isalpha()]
    sorted_chars = sorted(string, key=lambda char: -ord(char))[:76]
    return sorted_chars