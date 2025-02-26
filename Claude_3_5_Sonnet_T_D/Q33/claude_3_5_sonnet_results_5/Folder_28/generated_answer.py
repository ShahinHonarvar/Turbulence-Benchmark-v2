def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = []
    for char in s[41:50]:
        if char in vowels and 'W' < char <= '[':
            result.append(char)
    return result