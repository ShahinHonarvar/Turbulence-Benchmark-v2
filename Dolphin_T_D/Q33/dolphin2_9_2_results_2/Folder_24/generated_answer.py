def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [s[i] for i in range(23, 57) if s[i] in vowels and ord('0') < ord(s[i]) <= ord('d')]
    return result