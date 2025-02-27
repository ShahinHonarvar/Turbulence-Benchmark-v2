def return_n_greatest_chars(string):
    char_list = [(char, ord(char)) for char in string]
    char_list.sort(key=lambda x: x[1], reverse=True)
    return [char for char, _ in char_list[:46]]