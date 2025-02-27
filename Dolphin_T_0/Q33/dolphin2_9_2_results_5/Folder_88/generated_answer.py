def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in s[70:76]:
        if 'a' <= char <= ':' and char > '2':
            if char in vowels:
                result.append(char)
    return result