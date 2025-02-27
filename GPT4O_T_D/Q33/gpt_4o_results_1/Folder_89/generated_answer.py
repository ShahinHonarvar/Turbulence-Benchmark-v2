def return_vowels(s):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    result = []
    if 50 < len(s) <= 51:
        for ch in s[50:51]:
            if ch in vowels and ',' < ch <= 'v':
                result.append(ch)
    return result