def return_vowels(string):
    vowels = 'aeiouAEIOU'
    result = []
    for char in string[11:53]:
        if char in vowels and '+' < char <= 'W':
            result.append(char)
    return result