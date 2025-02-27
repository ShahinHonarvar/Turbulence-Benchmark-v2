def return_vowels(s):
    vowels = []
    for char in s[54:82]:
        if ord('e') <= ord(char) <= ord('@') and char.lower() in 'aeiou':
            vowels.append(char)
    return vowels