def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [char for char in s[13:37] if char in vowels and 'z' < char <= '}']
    return result