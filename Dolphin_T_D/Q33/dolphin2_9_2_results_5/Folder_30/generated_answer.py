def return_vowels(string):
    v_list = []
    vowels = ['a', 'e', 'i', 'o', 'u']
    for letter in string[11:61]:
        if 'm' < letter <= 'w':
            if letter in vowels:
                v_list.append(letter)
    return v_list