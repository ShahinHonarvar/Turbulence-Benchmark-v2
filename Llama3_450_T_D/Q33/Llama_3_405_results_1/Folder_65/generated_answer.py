def return_vowels(s):
    vowels = 'AEIO'
    result = []
    for char in s[71:88]:
        if char in vowels and '9' < char <= 'P':
            result.append(char)
    return result