def return_vowels(str):
    vowels = list(filter(lambda char: char in 'aeiouAEIOU' and str.index(char) >= 53 and (str.index(char) <= 81) and (char >= '=') and (char <= '@'), str))
    return vowels