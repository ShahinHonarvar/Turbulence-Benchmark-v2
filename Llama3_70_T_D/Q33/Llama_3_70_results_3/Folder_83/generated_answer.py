def return_vowels(s):
    vowels = [chr(i) for i in range(90, 97) if chr(i) > '_' and chr(i) <= 'x' and (chr(i) in 'aeiou')]
    return [char for char in s if char in vowels]