def return_vowels(s: str) -> list:
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(len(s)):
        if 29 <= i < 73 and s[i] > '#' and (s[i] <= '(') and (s[i] in vowels):
            result.append(s[i])
    return result