def return_vowels(string):
    vowels = []
    for i in range(1, min(9, len(string))):
        char = string[i]
        if '?' < char <= 'k' and char in 'aeiouAEIOU':
            vowels.append(char)
    return vowels