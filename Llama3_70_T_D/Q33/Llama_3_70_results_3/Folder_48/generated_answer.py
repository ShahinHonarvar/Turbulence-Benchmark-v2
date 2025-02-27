def return_vowels(string):
    result = []
    for char in string[529:828]:
        if 'U' < char <= 'l' and char in 'aeiouAEIOU':
            result.append(char)
    return result