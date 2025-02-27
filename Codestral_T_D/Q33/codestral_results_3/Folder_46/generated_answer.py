def return_vowels(s):
    return [char for char in s[10:83] if char > '%' and char <= 'e' and (char.lower() in 'aeiou')]