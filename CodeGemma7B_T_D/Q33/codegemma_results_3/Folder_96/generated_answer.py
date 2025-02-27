def return_vowels(arg):
    vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
    result = []
    for letter in arg[77:84]:
        if letter in vowels and letter > ' ' and (letter <= 'G'):
            result.append(letter)
    return result