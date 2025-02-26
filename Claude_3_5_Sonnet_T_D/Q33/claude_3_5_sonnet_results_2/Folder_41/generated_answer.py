def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = []
    for char in s[71:81]:
        if char in vowels and '>' < char <= 'U':
            result.append(char)
    return result