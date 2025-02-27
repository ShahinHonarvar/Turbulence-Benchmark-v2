def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = []
    for char in s[21:24]:
        if char > '-' and char <= 'n' and (char in vowels):
            result.append(char)
    return result