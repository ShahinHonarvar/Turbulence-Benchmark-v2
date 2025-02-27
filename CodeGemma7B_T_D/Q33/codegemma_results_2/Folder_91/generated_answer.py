def return_vowels(string):
    vowels = []
    for char in string[4:8]:
        if char.lower() in 'aeiou' and 'p' < char.lower() <= 'r':
            vowels.append(char)
    return vowels