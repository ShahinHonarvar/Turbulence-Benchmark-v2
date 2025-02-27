def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = []
    for char in s[64:82]:
        if char in vowels and 'P' < char <= 'z':
            result.append(char)
    return result