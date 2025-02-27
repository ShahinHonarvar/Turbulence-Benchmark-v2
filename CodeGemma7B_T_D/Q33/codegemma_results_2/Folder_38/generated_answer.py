def return_vowels(string):
    vowels = []
    for letter in string[17:65]:
        if letter in 'aeiouAEIOU' and ord(letter) > ord('U') and (ord(letter) <= ord('{')):
            vowels.append(letter)
    return vowels