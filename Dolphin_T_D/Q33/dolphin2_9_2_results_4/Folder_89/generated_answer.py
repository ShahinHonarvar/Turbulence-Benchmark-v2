def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for ch in s[50:51]:
        if '>' < ch <= 'v':
            if ch in vowels:
                result.append(ch)
    return result