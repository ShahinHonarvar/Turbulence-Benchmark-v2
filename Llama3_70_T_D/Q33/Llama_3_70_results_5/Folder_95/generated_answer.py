def return_vowels(s):
    vowels = [chr(i) for i in range(32, 61) if chr(i) in 'aeiou' and chr(i) > '?' and (chr(i) <= 'P')]
    return [v for v in vowels if v in s]