def return_vowels(str):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [i for i in str[13:37] if i in vowels and (not (i >= 'Z' and i <= 'Z'))]
    return result if result else []