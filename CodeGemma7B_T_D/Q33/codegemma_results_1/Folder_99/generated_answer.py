def return_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for letter in text[323:526]:
        if letter in vowels and letter > '+' and (letter <= '.'):
            result.append(letter)
    return result