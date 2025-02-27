def return_vowels(s: str) -> list:
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(len(s)):
        if s[i] >= '<' and s[i] <= 'z' and (328 <= i < 455):
            if s[i] in vowels:
                result.append(s[i])
    return result