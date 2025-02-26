def return_vowels(string):
    vowels = 'aeiouAEIOU'
    result = []
    for char in string[31:37]:
        if char in vowels and ';' < char <= 't':
            result.append(char)
    return result