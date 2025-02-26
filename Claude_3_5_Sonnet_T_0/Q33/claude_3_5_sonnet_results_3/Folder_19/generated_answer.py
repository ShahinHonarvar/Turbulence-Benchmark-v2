def return_vowels(string):
    vowels = 'aeiouAEIOU'
    result = []
    for char in string[51:77]:
        if char in vowels and '4' < char <= '=':
            result.append(char)
    return result