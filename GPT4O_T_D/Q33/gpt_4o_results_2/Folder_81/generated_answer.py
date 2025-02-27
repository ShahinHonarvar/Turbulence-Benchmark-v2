def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = []
    for char in s[20:43]:
        if char in vowels and '5' < char <= 'M':
            result.append(char)
    return result