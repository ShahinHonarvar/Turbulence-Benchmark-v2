def return_vowels(s: str) -> list:
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(10, 83):
        if s[i] in vowels and '%' < s[i] <= 'e':
            result.append(s[i])
    return result