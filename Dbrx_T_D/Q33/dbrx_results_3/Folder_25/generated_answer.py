def return_vowels(s: str) -> list:
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in s[28:76]:
        if char > '+' and char <= 'z' and (char in vowels):
            result.append(char)
    return result