def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    valid_vowels = []
    for i in range(483, 664):
        if string[i] in vowels and ord(string[i]) > ord('&') and (ord(string[i]) <= ord('h')):
            valid_vowels.append(string[i])
    return valid_vowels