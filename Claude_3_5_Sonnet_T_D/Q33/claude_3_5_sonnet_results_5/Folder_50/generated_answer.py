def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = []
    for char in s[11:53]:
        if char in vowels and '+' < char <= 'W':
            result.append(char)
    return result