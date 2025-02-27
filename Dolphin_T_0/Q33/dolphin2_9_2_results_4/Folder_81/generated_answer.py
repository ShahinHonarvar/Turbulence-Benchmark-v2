def return_vowels(s):
    return [char for char in s[20:43] if char > '5' and char <= 'M' and (char.lower() in 'aeiou')]