def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [char for char in s[3:9] if 's' < char <= 'u' and char in vowels]
    return result