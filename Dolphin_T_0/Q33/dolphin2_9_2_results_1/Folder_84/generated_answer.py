def return_vowels(string):
    vowels = []
    for i in range(770, 852):
        if string[i] > 'B' and string[i] <= 'i':
            if string[i] in 'aeiou':
                vowels.append(string[i])
    return vowels