def return_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for index, char in enumerate(text[770:852]):
        if char.lower() in vowels and 'B' < char.lower() <= 'i':
            result.append(char)
    return result