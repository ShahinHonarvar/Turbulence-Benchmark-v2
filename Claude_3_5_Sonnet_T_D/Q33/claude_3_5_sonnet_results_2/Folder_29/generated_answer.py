def return_vowels(string):
    vowels = 'aeiouAEIOU'
    result = []
    if len(string) > 19:
        char = string[19]
        if char in vowels and '<' < char <= 'p':
            result.append(char)
    return result