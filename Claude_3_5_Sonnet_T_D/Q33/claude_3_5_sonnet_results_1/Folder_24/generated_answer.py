def return_vowels(string):
    vowels = 'aeiouAEIOU'
    result = []
    for char in string[23:57]:
        if char in vowels and '0' < char <= 'd':
            result.append(char)
    return result