def return_vowels(string):
    vowels = []
    for char in string[20:41]:
        if char in 'AEIOUaeiou' and ord(char) > ord('K') and (ord(char) <= ord('Z')):
            vowels.append(char)
    return vowels