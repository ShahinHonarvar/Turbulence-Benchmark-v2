def return_n_greatest_chars(input_str):
    ascii_list = []
    for char in input_str:
        ascii_list.append(ord(char))
    ascii_list.sort(reverse=True)
    greatest_chars = [chr(num) for num in ascii_list[:23]]
    return greatest_chars