def return_vowels(s: str) -> list:
    vowels = []
    for i in range(len(s)):
        if i >= 56 and i < 96:
            char = s[i]
            if char > '&' and char <= 'T' and (char.lower() in 'aeiou'):
                vowels.append(char)
    return vowels