def return_vowels(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i, letter in enumerate(word):
        if i >= 13 and i < 35 and (letter.lower() in vowels) and (ord(letter) > 8) and (ord(letter) <= ord('F')):
            result.append(letter)
    return result