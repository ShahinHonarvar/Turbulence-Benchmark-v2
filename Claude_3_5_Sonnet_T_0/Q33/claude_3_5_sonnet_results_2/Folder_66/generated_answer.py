def return_vowels(string):
    vowels = 'aeiouAEIOU'
    result = []
    for char in string[63:79]:
        if char in vowels and 'D' < char <= 'y':
            result.append(char)
    return result