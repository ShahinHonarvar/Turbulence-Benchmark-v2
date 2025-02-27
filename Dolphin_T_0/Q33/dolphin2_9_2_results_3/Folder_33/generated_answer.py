def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [char for char in s[163:771] if ':' < char <= 'E' and char in vowels]