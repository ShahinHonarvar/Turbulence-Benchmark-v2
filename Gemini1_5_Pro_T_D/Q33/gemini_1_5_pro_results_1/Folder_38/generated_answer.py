def return_vowels(text):
    vowels = []
    for i in range(17, 65):
        if i < len(text) and text[i] in 'AEIOUaeiou' and (ord(text[i]) > ord('U')) and (ord(text[i]) <= ord('{')):
            vowels.append(text[i])
    return vowels