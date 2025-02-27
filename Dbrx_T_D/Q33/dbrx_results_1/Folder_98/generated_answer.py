def return_vowels(s: str) -> list:
    vowels = []
    for i in range(3, 9):
        if i >= 0 and i < len(s) and ('S' < s[i] <= 'U'):
            if s[i] in 'AEIOUaeiou':
                vowels.append(s[i])
    return vowels