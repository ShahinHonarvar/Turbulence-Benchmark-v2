def return_vowels(string):
    vowels = 'aeiouAEIOU'
    result = []
    for char in string[59:61]:
        if char in vowels and '+' < char <= 'h':
            result.append(char)
    return result