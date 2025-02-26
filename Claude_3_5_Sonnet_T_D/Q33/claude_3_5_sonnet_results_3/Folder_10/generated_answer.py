def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = []
    for char in s[31:37]:
        if char in vowels and ';' < char <= 't':
            result.append(char)
    return result