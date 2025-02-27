def return_vowels(string):
    vowels = []
    for char in string[19:32]:
        if ord(char) > ord('0') and ord(char) <= ord('7') and (char in 'aeiou'):
            vowels.append(char)
    return vowels