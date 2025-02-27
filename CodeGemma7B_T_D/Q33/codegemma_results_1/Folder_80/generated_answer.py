def return_vowels(arg):
    vowels = 'aeiouAEIOU'
    result = []
    for i, char in enumerate(arg[85:99]):
        if char in vowels and i >= 0 and (char != '/') and (char <= 'n'):
            result.append(char)
    return result