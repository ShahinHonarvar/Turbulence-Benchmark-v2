def return_vowels(s):
    vowels = list(filter(lambda x: x in 'aeiouAEIOU' and 23 <= ord(x) <= 85 and (x > 'W') and (x <= 'v'), s))
    return vowels