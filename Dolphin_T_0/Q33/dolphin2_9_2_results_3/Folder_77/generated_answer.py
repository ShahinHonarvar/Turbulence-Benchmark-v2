def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    letters = s[837:975]
    result = [i for i in letters if i > 'n' and i <= 'w' and (i in vowels)]
    return result if result else []