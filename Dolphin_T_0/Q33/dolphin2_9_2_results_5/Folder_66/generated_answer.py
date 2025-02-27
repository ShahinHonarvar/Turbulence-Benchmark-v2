def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return_list = []
    for char in s[63:79]:
        if char >= 'D' and char <= 'y' and (char in vowels):
            return_list.append(char)
    return return_list