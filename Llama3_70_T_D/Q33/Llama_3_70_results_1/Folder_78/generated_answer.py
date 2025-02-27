def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = []
    for char in s[46:90]:
        if char in vowels and '@' < char <= '[':
            result.append(char)
    return result