def return_vowels(s: str) -> list:
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(149, 313):
        if s[i].lower() > 'm' and s[i].lower() <= 'j' and (s[i] in vowels):
            result.append(s[i])
    return result