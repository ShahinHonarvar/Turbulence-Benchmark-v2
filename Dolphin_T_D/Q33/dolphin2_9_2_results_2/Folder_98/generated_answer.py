def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return_list = []
    for char in string[3:9]:
        if char >= 's' and char <= 'u':
            if char in vowels:
                return_list.append(char)
    return return_list