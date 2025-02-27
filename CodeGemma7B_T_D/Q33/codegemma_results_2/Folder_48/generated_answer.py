def return_vowels(s):
    return list(filter(lambda x: x in 'AEIOUaeiou' and 529 <= s.index(x) < 828 and (x > 'U') and (x <= 'l'), s))