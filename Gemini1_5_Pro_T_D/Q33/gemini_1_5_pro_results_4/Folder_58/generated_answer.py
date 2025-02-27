def return_vowels(text):
    vowels = []
    for i in range(260, 322):
        if i < len(text) and text[i] in 'AEIOUaeiou' and (ord(text[i]) > ord('%')) and (ord(text[i]) <= ord('U')):
            vowels.append(text[i])
    return vowels