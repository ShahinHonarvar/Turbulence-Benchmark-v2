def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = []
    for char in s[14:60]:
        if char in vowels and 'D' < char <= 'v':
            result.append(char)
    return result