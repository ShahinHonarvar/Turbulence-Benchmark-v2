def return_vowels(s):
    vowels = [chr(i) for i in range(86, 100) if chr(i) > 'E' and chr(i) <= 'r' and (chr(i) in 'aeiou')]
    return vowels