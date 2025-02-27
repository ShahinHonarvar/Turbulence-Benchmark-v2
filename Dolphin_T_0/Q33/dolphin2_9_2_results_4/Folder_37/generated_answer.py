def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = []
    for char in s[82:90]:
        if 'T' < char <= 'b' and char in vowels:
            result.append(char)
    return result