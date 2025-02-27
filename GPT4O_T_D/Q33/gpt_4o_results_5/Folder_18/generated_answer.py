def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = []
    for char in s[528:606]:
        if char in vowels and 'M' < char <= 'X':
            result.append(char)
    return result