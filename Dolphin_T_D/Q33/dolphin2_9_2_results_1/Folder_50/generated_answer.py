def return_vowels(s):
    vowels = []
    for char in s[11:53]:
        if char.isalpha() and char.lower() in 'aeiou' and ('+' < char <= 'W'):
            vowels.append(char)
    return vowels