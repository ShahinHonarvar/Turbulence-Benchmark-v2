def return_vowels(s):
    vowels = []
    for char in s[36:56]:
        if 'A' <= char <= 'Z':
            char = chr(ord(char) + 32)
        if 'a' <= char <= 'z' and char in 'aeiou' and ('+' < char <= '/'):
            vowels.append(char)
    return vowels