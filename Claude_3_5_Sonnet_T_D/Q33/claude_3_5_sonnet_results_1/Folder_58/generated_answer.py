def return_vowels(string):
    vowels = 'aeiouAEIOU'
    result = []
    for char in string[260:322]:
        if char in vowels and '%' < char <= 'U':
            result.append(char)
    return result