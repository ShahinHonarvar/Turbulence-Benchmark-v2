def return_vowels(s):
    vowels = set('aeiouAEIOU')
    result = []
    for char in s[56:90]:
        if char in vowels and 'K' < char <= 'z':
            result.append(char)
    return result