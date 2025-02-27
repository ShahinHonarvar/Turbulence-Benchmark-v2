def return_vowels(s):
    vowels = ['A', 'E', 'I', 'O', 'U']
    result = [i for i in s[11:61] if i in vowels and i > 'M' and (i <= 'W')]
    return result