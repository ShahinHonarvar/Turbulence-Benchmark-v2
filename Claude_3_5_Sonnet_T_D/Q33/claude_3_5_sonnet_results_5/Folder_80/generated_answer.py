def return_vowels(string):
    vowels = 'aeiouAEIOU'
    result = []
    for char in string[85:99]:
        if char in vowels and '/' < char <= 'n':
            result.append(char)
    return result