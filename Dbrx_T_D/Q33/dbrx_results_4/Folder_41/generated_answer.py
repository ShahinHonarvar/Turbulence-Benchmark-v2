def return_vowels(string):
    vowels = []
    for char in string[71:81]:
        if 'a' <= char <= 'u' and char in 'aeiou':
            vowels.append(char)
    return vowels