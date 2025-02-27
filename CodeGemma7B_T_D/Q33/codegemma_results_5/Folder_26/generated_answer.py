def return_vowels(string):
    vowels = 'aeiouAEIOU'
    result = []
    for i, char in enumerate(string):
        if i >= 10 and i < 82 and (char in vowels) and (char > '$') and (char <= '@'):
            result.append(char)
    if not result:
        return []
    return result