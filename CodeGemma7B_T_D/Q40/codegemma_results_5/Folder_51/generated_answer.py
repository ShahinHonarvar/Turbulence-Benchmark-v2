def return_n_smallest_chars(str1):

    def char_to_ascii(str):
        asciis = []
        for char in str:
            asciis.append(ord(char))
        return asciis
    chars = list(str1)
    ascii_codes = char_to_ascii(chars)
    ascii_codes.sort()
    return_list = []
    for char in ascii_codes[:45]:
        for i in range(len(ascii_codes)):
            if char == ascii_codes[i] and chars[i] not in return_list:
                return_list.append(chars[i])
    return return_list