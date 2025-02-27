def return_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    filtered_vowels = []
    for i in range(10, 83):
        if text[i] in vowels and ord(text[i]) % 4 != 0 and (ord(text[i]) <= ord('e')):
            filtered_vowels.append(text[i])
    return filtered_vowels