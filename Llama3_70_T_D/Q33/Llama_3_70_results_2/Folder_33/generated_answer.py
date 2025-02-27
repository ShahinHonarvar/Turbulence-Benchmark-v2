def return_vowels(s):
    vowels = [chr(i) for i in range(ord(':') + 1, ord('E') + 1) if chr(i) in 'AEIOU']
    return [char for char in s[163:771] if char in vowels]