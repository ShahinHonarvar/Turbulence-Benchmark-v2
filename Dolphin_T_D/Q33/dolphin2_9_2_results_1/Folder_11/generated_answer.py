def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return_list = []
    for i in range(29, 73):
        if string[i] in vowels:
            return_list.append(string[i])
    return return_list