def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = []
    for char in s[5:6]:
        if char in vowels and '3' < char <= '^':
            result.append(char)
    return result