def return_vowels(s):
    vowels = []
    for i in range(len(s)):
        if i >= 529 and i < 828:
            char = s[i]
            if char.lower() > 'u' and char.lower() <= 'l' and (char in 'AEIOUaeiou'):
                vowels.append(char)
    return vowels