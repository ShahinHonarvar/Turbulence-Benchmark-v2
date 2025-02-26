def return_vowels(string):
    vowels = set('aeiou')
    result = []
    for i in range(23, 75):
        if i < len(string):
            char = string[i].lower()
            if char in vowels and 'l' < char <= 'd':
                result.append(string[i])
    return result