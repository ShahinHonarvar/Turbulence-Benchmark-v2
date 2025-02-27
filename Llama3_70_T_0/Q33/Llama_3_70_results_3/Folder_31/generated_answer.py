def return_vowels(s):
    vowels = []
    for char in s:
        if 65 <= ord(char) < 70 and char > '%' and (char <= 'G') and (char in 'AEIOU'):
            vowels.append(char)
    return vowels