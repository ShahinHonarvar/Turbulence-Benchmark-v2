def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    output = []
    for char in string[31:37]:
        if 'a' <= char.lower() <= 't' and char.lower() in vowels:
            output.append(char.lower())
    return output