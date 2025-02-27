def return_vowels(str):
    vowels = []
    for char in str[47:89]:
        if char.lower() in 'aeiou' and char > '@' and (char <= 'n'):
            vowels.append(char.lower())
    return vowels