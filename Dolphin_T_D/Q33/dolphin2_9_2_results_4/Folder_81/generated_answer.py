def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    target_chars = []
    for char in string[20:43]:
        if 'a' <= char <= 'm' and char in vowels:
            target_chars.append(char)
    return target_chars