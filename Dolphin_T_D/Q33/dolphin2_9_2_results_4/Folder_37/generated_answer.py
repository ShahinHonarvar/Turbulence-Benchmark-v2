def return_vowels(string):
    vowels = []
    for char in string[82:90]:
        if char > 'T' and char <= 'b':
            if char.lower() in 'aeiou':
                vowels.append(char)
    return vowels