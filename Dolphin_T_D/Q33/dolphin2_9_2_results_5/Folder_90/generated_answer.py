def return_vowels(s):
    range_s = s[142:145]
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [char for char in range_s if 'a' <= char <= 'o' and char in vowels]
    return result