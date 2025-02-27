def return_vowels(string):
    vowels = []
    for char in string[50:51]:
        if 'a' <= char <= 'v' and char in 'aeiou':
            vowels.append(char)
    return vowels