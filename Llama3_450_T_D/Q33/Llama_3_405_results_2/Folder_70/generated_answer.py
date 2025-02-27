def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = []
    for char in s[171:402]:
        if char in vowels and 'I' < char <= 'k':
            result.append(char)
    return result