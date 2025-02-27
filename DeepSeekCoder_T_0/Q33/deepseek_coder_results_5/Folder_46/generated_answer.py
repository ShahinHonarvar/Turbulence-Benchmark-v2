def return_vowels(s):
    vowels = []
    for char in s[10:83]:
        if 'a' <= char <= 'e' and char > '%':
            vowels.append(char)
    return vowels