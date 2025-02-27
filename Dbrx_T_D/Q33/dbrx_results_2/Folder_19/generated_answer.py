def return_vowels(s: str) -> list:
    vowels = []
    for i in range(51, 77):
        if s[i] > '4' and s[i] <= '=':
            if s[i] in 'aeiouAEIOU':
                vowels.append(s[i])
    return vowels