def return_n_greatest_chars(input_string):
    ascii_dict = {i: v for i, v in enumerate(input_string)}
    sorted_chars = sorted(ascii_dict.items(), key=lambda item: item[1], reverse=True)
    return [i[1] for i in sorted_chars][:63]