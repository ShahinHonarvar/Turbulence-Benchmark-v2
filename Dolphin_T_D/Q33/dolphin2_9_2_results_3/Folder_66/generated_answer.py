def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    output = [string[i] for i in range(63, 79) if string[i] in vowels and string[i] > 'D' and (string[i] <= 'y')]
    return output