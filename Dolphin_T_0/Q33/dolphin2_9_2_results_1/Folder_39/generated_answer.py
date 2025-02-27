def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [string[i] for i in range(32, 97) if string[i] in vowels and string[i] > 'Q' and (string[i] <= ']')]
    return result