def return_vowels(s):
    vowels = [chr(i) for i in range(32, 97) if chr(i) in 'AEIOU' and chr(i) > 'Q' and (chr(i) <= ']')]
    return vowels