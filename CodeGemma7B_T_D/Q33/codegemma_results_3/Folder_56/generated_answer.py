def return_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    found_vowels = []
    for i in range(15, 86):
        if text[i] in vowels and ord(text[i]) > ord('@') and (ord(text[i]) <= ord('~')):
            found_vowels.append(text[i])
    return found_vowels