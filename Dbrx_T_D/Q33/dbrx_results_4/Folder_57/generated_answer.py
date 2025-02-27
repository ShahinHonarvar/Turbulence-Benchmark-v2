def return_vowels(s: str) -> list:
    vowels = []
    for i in range(len(s)):
        if 21 <= i < 23 and 'aeiouAEIOU' > s[i] > '-' and (s[i] <= 'n'):
            vowels.append(s[i])
    return vowels