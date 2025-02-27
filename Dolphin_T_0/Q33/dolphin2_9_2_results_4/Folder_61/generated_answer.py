def return_vowels(s):
    vowels = [i for i in s[1:4] if 'C' < i <= 'I' and i.lower() in 'aeiou']
    return vowels