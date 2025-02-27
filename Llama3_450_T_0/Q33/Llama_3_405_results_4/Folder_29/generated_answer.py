def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = []
    for char in s[19:20]:
        if char in vowels and '<' < char <= 'p':
            result.append(char)
    return result