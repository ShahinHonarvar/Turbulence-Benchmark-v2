def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for character in string[29:73]:
        if character > 'a' and character <= '.':
            if character in vowels:
                result.append(character)
    return result