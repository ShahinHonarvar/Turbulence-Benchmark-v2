def return_vowels(text):
    vowels = []
    for i in range(20, 43):
        if i < len(text) and text[i] in 'AEIOUaeiou' and (ord(text[i]) > ord('5')) and (ord(text[i]) <= ord('M')):
            vowels.append(text[i])
    return vowels