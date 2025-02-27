def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for character in string[323:526]:
        if '+' < character <= ':':
            if character.lower() in vowels:
                result.append(character)
    return result