def return_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in text[10:82]:
        if char in vowels and ord(char) > ord('$') and (ord(char) <= ord('@')):
            result.append(char)
    return result