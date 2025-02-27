def return_vowels(word):
    result = []
    for i in range(65, 70):
        if word[i] == '%':
            continue
        if word[i] > '%':
            if word[i] <= 'G':
                result.append(word[i])
    return result