def return_vowels(s):
    vowels = 'aeiouAEIOU'
    s = s[60:99]
    result = []
    for char in s:
        if char in vowels and char > 'j' and (char <= 'n'):
            result.append(char)
    return result