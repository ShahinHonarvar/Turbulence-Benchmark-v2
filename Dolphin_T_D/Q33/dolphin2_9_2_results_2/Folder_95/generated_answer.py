def return_vowels(string):
    vowels = []
    for char in string[32:61]:
        if '?' < char <= 'P':
            if char.lower() in ['a', 'e', 'i', 'o', 'u']:
                vowels.append(char)
    return vowels