def return_vowels(text):
    vowels = []
    for i in range(41, 50):
        if i < len(text) and text[i] in 'AEIOUaeiou' and (ord(text[i]) > ord('W')) and (ord(text[i]) <= ord('[')):
            vowels.append(text[i])
    return vowels