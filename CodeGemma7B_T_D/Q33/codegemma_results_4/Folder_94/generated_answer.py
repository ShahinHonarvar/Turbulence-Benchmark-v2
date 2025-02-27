def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    word = []
    for letter in string:
        if letter.lower() in vowels:
            if ord(letter.lower()) > 4 and ord(letter.lower()) <= 72:
                word.append(letter.lower())
    return word