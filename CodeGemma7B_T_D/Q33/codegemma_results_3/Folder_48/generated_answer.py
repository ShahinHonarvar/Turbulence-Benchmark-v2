def return_vowels(text):
    vowels = 'aeiouAEIOU'
    output = []
    for letter in text[529:828]:
        if letter in vowels and letter > 'U' and (letter <= 'l'):
            output.append(letter)
    if not output:
        output = []
    return output