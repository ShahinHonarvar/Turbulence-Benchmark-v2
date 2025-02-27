def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [char for char in s[40:94] if char > '4' and char <= 'H' and (char in vowels)]
    return result