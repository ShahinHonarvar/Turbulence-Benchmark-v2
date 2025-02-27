def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for ch in s[41:50]:
        if ch > 'W' and ch <= '[':
            if ch in vowels:
                result.append(ch)
    return result