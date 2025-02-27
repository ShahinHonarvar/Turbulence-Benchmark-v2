def return_vowels(s: str) -> list:
    vowels = []
    for i in range(len(s)):
        if i >= 24 and i < 59:
            if s[i] > 'N' and s[i] <= 'U':
                if s[i] in 'AEIOUaeiou':
                    vowels.append(s[i])
    return vowels