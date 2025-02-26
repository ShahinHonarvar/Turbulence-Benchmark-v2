def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = []
    for char in s[47:61]:
        if char in vowels and '9' < char <= 'O':
            result.append(char)
    return result