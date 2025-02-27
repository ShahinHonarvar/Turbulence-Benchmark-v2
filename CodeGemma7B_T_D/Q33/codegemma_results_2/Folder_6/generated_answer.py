def return_vowels(string):
    vowels = ''
    for char in string[20:34]:
        if char.lower() in 'aeiou' and (char > 'U' and char <= 'i'):
            vowels += char
    return vowels if vowels else []