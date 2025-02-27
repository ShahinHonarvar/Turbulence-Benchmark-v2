def return_vowels(s: str) -> list:
    vowels = []
    if len(s) >= 275:
        for i in range(273, 275):
            char = s[i]
            if char > '+' and char <= 'o' and (char.lower() in 'aeiou'):
                vowels.append(char)
    return vowels