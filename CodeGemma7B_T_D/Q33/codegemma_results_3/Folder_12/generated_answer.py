def return_vowels(a):
    b = list(a)
    vowels = ['A', 'E', 'I', 'O', 'U']
    result = []
    for letter in b[13:37]:
        if letter in vowels and letter >= '{' and (letter <= '~'):
            result.append(letter)
    return result