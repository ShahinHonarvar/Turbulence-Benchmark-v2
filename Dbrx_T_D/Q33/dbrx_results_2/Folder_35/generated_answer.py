def return_vowels(s):
    vowels = []
    for c in s[483:664]:
        if 'a' <= c <= 'h' and c in 'aeiou':
            vowels.append(c)
    return vowels