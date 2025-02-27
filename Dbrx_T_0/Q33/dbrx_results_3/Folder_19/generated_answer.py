def return_vowels(s: str) -> list:
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(len(s)):
        if 51 <= i < 77 and 4 < ord(s[i]) <= ord('=') and (s[i] in vowels):
            result.append(s[i])
    return result