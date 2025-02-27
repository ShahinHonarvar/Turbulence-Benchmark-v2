def return_vowels(inp_str):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    temp = inp_str[50:77]
    temp = [i for i in temp if i >= '#' and i <= 'r']
    return [i for i in temp if i in vowels]