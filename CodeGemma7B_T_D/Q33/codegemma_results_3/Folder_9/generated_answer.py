def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for letter in vowels:
        for index, value in enumerate(string):
            if letter == value and index >= 13 and (index < 35) and (ord(value) > 8) and (ord(value) <= ord('F')):
                result.append(value)
    return result