def return_vowels(s: str) -> list:
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in s[85:99]:
        if '/' < char <= 'n' and char in vowels:
            result.append(char)
    return result