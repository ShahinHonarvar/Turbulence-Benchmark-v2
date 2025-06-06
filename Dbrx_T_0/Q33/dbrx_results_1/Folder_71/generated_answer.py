def return_vowels(s: str) -> list:
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(len(s)):
        if s[i] > '+' and s[i] <= '/' and (i >= 36) and (i < 56) and (s[i] in vowels):
            result.append(s[i])
    return result