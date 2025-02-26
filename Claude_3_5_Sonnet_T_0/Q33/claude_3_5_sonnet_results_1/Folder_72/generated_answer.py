def return_vowels(string):
    vowels = 'aeiouAEIOU'
    result = []
    for char in string[37:57]:
        if char in vowels and '*' < char <= 'P':
            result.append(char)
    return result