def return_vowels(str):
    vowels = ['a', 'e', 'i', 'o', 'u']
    x = [i for i in str if i in vowels and str.index(i) >= 1 and (str.index(i) <= 9) and (i > str[0]) and (i <= str[9])]
    return x