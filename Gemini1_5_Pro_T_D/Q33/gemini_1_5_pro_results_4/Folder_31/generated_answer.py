def return_vowels(text):
    vowels = []
    for char in text:
        if 65 <= ord(char) < 70 and char > '%' and (char <= 'G'):
            vowels.append(char)
    return vowels