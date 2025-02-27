def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return_list = []
    for letter in string[3:8]:
        if '>' < letter <= 'D':
            if letter.lower() in vowels:
                return_list.append(letter)
    return return_list