def return_vowels(string):
    vowels = []
    for i in range(36, 56):
        if string[i].lower() in 'aeiou' and string[i] + '' not in vowels and (string[i] <= '/'):
            vowels.append(string[i])
    return vowels