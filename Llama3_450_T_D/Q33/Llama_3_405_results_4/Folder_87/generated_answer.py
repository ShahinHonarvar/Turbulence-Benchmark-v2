def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = []
    for char in s[34:58]:
        if char in vowels and 'b' < char <= 'o':
            result.append(char)
    return result