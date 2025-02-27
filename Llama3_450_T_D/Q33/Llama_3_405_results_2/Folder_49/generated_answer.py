def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = []
    for char in s[10:97]:
        if char in vowels and 'R' < char <= 'b':
            result.append(char)
    return result