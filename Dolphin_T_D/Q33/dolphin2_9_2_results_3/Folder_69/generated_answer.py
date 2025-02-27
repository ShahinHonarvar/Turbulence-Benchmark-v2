def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in string[641:872]:
        if '>' < char <= 'q' and char in vowels:
            result.append(char)
    return result