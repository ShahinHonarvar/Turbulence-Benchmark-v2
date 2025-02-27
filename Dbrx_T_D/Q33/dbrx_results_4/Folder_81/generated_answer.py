def return_vowels(s: str) -> list:
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in s[20:43]:
        if char > '5' and char <= 'M' and (char in vowels):
            result.append(char)
    return result