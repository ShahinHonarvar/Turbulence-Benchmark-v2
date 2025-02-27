def return_vowels(string):
    vowels = ['A', 'E', 'I', 'O', 'U']
    res_list = []
    for char in string[13:35]:
        if 8 < ord(char) <= ord('F') and char in vowels:
            res_list.append(char)
    return res_list