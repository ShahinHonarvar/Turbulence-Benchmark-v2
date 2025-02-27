def return_vowels(s: str) -> list:
    vowels = ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u']
    result = []
    for char in s[32:61]:
        if char > '?' and char <= 'P' and (char in vowels):
            result.append(char)
    return result