def return_vowels(string):
    vowels = 'aeiouAEIOU'
    result = []
    for char in string[56:68]:
        if char in vowels and 'M' < char <= 'X':
            result.append(char)
    return result