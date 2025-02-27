def return_vowels(s):
    vowels = [chr(i) for i in range(ord('A'), ord('Z') + 1) if chr(i) in 'AEIOU']
    return [char for char in s[74:96] if char in vowels and char > 'I' and (char <= 'X')]