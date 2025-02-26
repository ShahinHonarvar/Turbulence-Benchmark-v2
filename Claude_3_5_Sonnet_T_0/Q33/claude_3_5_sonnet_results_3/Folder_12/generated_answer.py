def return_vowels(string):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(13, 37):
        if i < len(string):
            char = string[i]
            if char in vowels and 'Z' < char <= '}':
                result.append(char)
    return result