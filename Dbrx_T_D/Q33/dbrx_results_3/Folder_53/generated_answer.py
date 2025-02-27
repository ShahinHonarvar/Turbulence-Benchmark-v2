def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [char for char in s[27:57] if char > 'o' and char <= 'w' and (char in vowels)]
    return result