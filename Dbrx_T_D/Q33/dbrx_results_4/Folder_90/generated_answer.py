def return_vowels(s: str) -> list:
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(142, 145):
        if i >= len(s):
            break
        char = s[i]
        if '4' < char <= 'o' and char in vowels:
            result.append(char)
    return result