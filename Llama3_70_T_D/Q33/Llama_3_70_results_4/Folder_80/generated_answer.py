def return_vowels(s):
    vowels = [chr(i) for i in range(85, 99) if chr(i) > '/' and chr(i) <= 'n' and (chr(i) in 'aeiou')]
    return vowels