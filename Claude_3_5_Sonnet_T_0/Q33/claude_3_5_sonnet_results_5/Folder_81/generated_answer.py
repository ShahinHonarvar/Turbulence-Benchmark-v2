def return_vowels(string):
    vowels = 'aeiouAEIOU'
    result = []
    for char in string[20:43]:
        if char in vowels and '5' < char <= 'M':
            result.append(char)
    return result