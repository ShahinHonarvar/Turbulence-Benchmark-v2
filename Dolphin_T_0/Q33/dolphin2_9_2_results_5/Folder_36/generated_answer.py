def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [s[i] for i in range(604, 949) if s[i] in vowels and ord('N') < ord(s[i]) <= ord('U')]
    return result