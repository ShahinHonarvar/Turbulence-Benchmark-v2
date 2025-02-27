def return_vowels(s):
    vowels = []
    for char in s[13:35]:
        if 8 < ord(char) <= 15 and char.lower() in 'aeiou':
            vowels.append(char)
    return vowels