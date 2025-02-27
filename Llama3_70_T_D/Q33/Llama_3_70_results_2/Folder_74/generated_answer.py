def return_vowels(s):
    result = []
    for char in s[69:82]:
        if 'a' <= char <= 'z' and char in 'aeiou':
            result.append(char)
        elif 'A' <= char <= 'Z' and char in 'AEIOU':
            result.append(char)
    return result