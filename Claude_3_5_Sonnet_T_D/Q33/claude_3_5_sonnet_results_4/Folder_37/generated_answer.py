def return_vowels(string):
    vowels = 'aeiouAEIOU'
    result = []
    for char in string[82:90]:
        if char in vowels and 'T' < char <= 'b':
            result.append(char)
    return result