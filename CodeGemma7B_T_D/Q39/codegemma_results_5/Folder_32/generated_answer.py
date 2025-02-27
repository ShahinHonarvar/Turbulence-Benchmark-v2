def return_n_greatest_chars(str_of_chars):
    list_of_tuples = []
    list_of_greatest_chars = []
    for char in str_of_chars:
        list_of_tuples.append(tuple((char, ord(char))))
    list_of_tuples.sort(key=lambda char: char[1], reverse=True)
    for i in range(8):
        list_of_greatest_chars.append(list_of_tuples[i][0])
    return list_of_greatest_chars