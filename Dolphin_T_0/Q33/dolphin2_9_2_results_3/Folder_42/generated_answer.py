def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for character in s[12:39]:
        if character > ';' and character <= '|':
            if character.lower() in vowels:
                result.append(character)
    return result