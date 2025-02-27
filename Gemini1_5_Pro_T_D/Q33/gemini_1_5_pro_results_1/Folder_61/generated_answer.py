def return_vowels(string):
    vowels = []
    for i in range(1, 3):
        if string[i] in 'AEIOUaeiou' and ord(string[i]) > ord('C') and (ord(string[i]) <= ord('I')):
            vowels.append(string[i])
    return vowels