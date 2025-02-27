def return_vowels(s):
    return [i for i in s[1:4] if i in 'AEIOUaeiou' and i > 'C' and (i <= 'I')]