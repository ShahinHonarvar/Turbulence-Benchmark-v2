def return_vowels(s):
    return [char for char in s[163:771] if char > ':' and char <= 'E' and (char.lower() in 'aeiou')]