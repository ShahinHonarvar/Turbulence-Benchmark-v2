def return_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for c in text[32:61]:
        if ord('P') >= ord(c) > ord('?') and c in vowels:
            result.append(c)
    return result