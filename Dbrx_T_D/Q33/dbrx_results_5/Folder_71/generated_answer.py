def return_vowels(s: str) -> list:
    vowels = []
    for i in range(len(s)):
        if i >= 36 and i < 56:
            if s[i] > '+' and s[i] <= '/':
                if s[i] in 'aeiouAEIOU':
                    vowels.append(s[i])
    return vowels