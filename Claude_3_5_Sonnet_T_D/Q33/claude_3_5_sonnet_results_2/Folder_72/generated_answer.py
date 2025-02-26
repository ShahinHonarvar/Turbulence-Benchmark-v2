def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = []
    for char in s[37:57]:
        if char in vowels and '*' < char <= 'P':
            result.append(char)
    return result