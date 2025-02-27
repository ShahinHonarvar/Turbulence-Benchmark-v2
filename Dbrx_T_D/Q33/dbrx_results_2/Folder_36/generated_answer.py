def return_vowels(s: str) -> list[str]:
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(604, 949):
        if s[i] in vowels and 'n' < s[i] <= 'U':
            result.append(s[i])
    return result