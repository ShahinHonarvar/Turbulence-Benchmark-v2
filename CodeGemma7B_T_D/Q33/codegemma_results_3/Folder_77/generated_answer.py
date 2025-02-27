def return_vowels(str):
    vowels = ['A', 'E', 'I', 'O', 'U']
    vowels_list = []
    for letter in str[837:975]:
        if letter in vowels and letter > 'N' and (letter <= 'W'):
            vowels_list.append(letter)
    return vowels_list