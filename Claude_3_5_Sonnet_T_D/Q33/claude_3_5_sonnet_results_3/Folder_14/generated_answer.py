def return_vowels(string):
    vowels = 'aeiouAEIOU'
    result = []
    for char in string[47:61]:
        if char in vowels and '9' < char <= 'O':
            result.append(char)
    return result