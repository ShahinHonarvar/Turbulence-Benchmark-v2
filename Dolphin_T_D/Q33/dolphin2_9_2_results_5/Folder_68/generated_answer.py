def return_vowels(my_str):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return_list = []
    for char in my_str[1:9]:
        if char > '?' and char <= 'k':
            if char in vowels:
                return_list.append(char)
    return return_list