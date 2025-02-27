def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    indices = [i for i in range(77, 84) if string[i] in vowels and vowels.index(string[i]) >= vowels.index('c') and (vowels.index(string[i]) <= vowels.index('G'))]
    return [string[i] for i in indices]