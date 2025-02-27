def return_vowels(s):
    return [char for char in s[3:9] if char in 'AEIOU' and char > 'S' and (char <= 'U')]