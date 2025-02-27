def return_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(40, 94):
        if text[i] in vowels and ord(text[i]) > ord('4') and (ord(text[i]) <= ord('H')):
            result.append(text[i])
    return result