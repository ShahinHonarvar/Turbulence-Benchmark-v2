def return_n_greatest_chars(string):
    list_of_ascii_values = []
    list_of_char = []
    final_list = []
    for Character in string:
        list_of_ascii_values.append(ord(Character))
        list_of_char.append(Character)
    zip_iterator = zip(list_of_ascii_values, list_of_char)
    tuple_of_list = sorted(zip_iterator, reverse=True)
    for k in range(len(tuple_of_list)):
        final_list.append(tuple_of_list[k][1])
    final_list = final_list[0:59]
    final_list.reverse()
    return final_list