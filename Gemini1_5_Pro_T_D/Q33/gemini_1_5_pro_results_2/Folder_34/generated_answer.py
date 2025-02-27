def return_vowels(string):
    vowels = []
    for i in range(19, 32):
        if i < len(string) and 'a' <= string[i] <= 'z' and (string[i] in 'aeiou') and (ord(string[i]) > ord('0')) and (ord(string[i]) <= ord('7')):
            vowels.append(string[i])
    return vowels