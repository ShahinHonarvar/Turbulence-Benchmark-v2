def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [letter for letter in s[4:8] if 'p' < letter <= 'r' and letter in vowels]
    return result