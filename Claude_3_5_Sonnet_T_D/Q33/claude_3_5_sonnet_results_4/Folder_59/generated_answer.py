def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    if len(string) > 8:
        for char in string[8:9]:
            if char.lower() in vowels and 'Y' < char <= 's':
                result.append(char)
    return result