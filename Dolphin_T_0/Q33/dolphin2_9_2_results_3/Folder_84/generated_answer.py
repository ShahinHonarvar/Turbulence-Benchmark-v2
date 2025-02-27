def return_vowels(string):
    vowels = []
    for char in string[770:852]:
        if 'B' < char <= 'i' and char.lower() in 'aeiou':
            vowels.append(char)
    return vowels