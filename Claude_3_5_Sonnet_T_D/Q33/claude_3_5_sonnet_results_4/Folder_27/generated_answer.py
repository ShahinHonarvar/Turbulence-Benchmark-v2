def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in string[29:31]:
        if char.lower() in vowels and 'a' < char.lower() <= 'f':
            result.append(char)
    return result