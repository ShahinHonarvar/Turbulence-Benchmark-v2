def return_vowels(s):
    vowels = []
    for char in s[64:82]:
        if 'A' <= char <= 'Z' or 'a' <= char <= 'z':
            if char in 'AEIOUaeiou':
                if char > 'P' and char <= 'z':
                    vowels.append(char)
    return vowels