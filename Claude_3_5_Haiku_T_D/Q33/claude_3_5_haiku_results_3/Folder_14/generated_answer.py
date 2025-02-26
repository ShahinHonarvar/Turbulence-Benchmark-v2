def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    result = [char for char in s[47:61] if char in vowels and char > '9' and (char <= 'O')]
    return result