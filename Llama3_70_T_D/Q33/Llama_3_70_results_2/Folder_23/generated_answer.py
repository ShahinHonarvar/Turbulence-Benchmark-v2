def return_vowels(string):
    vowels = []
    for char in string:
        if ord(char) >= 56 and ord(char) < 96 and (ord(char) > ord('&')) and (ord(char) <= ord('T')):
            if char in 'AEIOUaeiou':
                vowels.append(char)
    return vowels