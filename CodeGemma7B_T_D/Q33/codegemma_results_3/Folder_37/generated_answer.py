def return_vowels(text):
    result = []
    for letter in text[82:90]:
        if letter.lower() in 'aeiou' and letter.lower() > 't' and (letter.lower() <= 'b'):
            result.append(letter.lower())
    return result