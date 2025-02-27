def return_vowels(string):
    result = []
    for i in range(21, 59):
        if string[i] > '/' and string[i] <= 'a':
            if string[i].lower() in 'aeiou':
                result.append(string[i])
    return result