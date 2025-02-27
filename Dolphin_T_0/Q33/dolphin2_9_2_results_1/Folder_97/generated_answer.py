def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [string[i] for i in range(328, 455) if '>' < string[i] <= 'z' and string[i] in vowels]