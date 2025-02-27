def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for ch in s[46:49]:
        if '[' < ch <= 'p':
            if ch in vowels:
                result.append(ch)
    return result