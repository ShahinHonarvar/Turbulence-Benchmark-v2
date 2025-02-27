def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = []
    for char in s[495:837]:
        if char > 'B' and char <= 't' and (char in vowels):
            result.append(char)
    return result