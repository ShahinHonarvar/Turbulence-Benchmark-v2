def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    if len(s) >= 51:
        for char in s[50:51]:
            if char in vowels and ',' < char <= 'v':
                result.append(char)
    return result