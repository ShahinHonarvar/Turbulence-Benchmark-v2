def return_vowels(string):
    vowels = []
    for i in range(3, 8):
        if i < len(string) and ';' < string[i] <= 'D':
            if string[i] in 'AEIOUaeiou':
                vowels.append(string[i])
    return vowels