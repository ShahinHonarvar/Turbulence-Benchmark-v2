def return_vowels(in_str):
    vowels = ['a', 'e', 'i', 'o', 'u']
    out_list = []
    for char in in_str[24:64]:
        if 'f' < char <= 'h' and char in vowels:
            out_list.append(char)
    return out_list