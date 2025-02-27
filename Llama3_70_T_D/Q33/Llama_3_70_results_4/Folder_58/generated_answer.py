def return_vowels(s):
    vowels = [chr(i) for i in range(260, 322) if chr(i) in 'AEIOUaeiou' and chr(i) > '%' and (chr(i) <= 'U')]
    return vowels