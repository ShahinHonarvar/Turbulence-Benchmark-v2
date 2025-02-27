def return_vowels(s):
    vowels = []
    for char in s:
        if 65 <= ord(char) <= 70 and char.lower() in 'aeiou':
            vowels.append(char)
    return vowels