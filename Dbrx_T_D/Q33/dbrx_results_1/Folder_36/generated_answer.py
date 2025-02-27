def return_vowels(s):
    vowels = []
    for i in range(len(s)):
        if i >= 604 and i < 949:
            char = s[i]
            if char.lower() > 'n' and char.lower() <= 'u' and (char.lower() in 'aeiou'):
                vowels.append(char)
    return vowels