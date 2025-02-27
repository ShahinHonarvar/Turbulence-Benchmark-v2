def return_vowels(string):
    vowels = []
    for i in range(41, 50):
        if i < len(string) and string[i] in 'AEIOUaeiou' and (ord(string[i]) > ord('W')) and (ord(string[i]) <= ord('[')):
            vowels.append(string[i])
    return vowels