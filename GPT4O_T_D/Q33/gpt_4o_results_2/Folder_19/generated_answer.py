def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = []
    for char in s[51:77]:
        if char in vowels and '4' < char <= '=':
            result.append(char)
    return result