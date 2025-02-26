def return_vowels(string):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(47, 89):
        if i < len(string):
            char = string[i]
            if char in vowels and '@' < char <= 'n':
                result.append(char)
    return result