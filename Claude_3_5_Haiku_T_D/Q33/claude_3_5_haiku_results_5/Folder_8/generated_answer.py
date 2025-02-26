def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for index, char in enumerate(string):
        if 64 <= index < 82 and char.lower() in vowels and ('p' < char.lower() <= 'z'):
            result.append(char)
    return result