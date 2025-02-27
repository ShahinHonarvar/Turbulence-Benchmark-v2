def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in string[1:7]:
        if 'F' < char <= 'j' and char in vowels:
            result.append(char)
    return result