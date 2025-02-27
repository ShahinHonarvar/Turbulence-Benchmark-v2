def return_vowels(s):
    vowels = 'aeiouAEIOU'
    valid_chars = [chr(i) for i in range(ord('2') + 1, ord(':') + 1)]
    return [char for char in s[70:76] if char in vowels and char in valid_chars]