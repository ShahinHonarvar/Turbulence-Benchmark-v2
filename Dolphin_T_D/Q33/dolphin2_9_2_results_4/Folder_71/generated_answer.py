def return_vowels(string):
    vowels_in_range = ['a', 'e', 'i', 'o', 'u']
    letters_in_range = string[36:56]
    return_list = []
    for letter in letters_in_range:
        if '+' < letter <= '/' and letter in vowels_in_range:
            return_list.append(letter)
    return return_list