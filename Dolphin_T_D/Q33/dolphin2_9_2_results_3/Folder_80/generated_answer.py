def return_vowels(s):
    vowels = []
    for char in s[85:99]:
        if '/' < char <= 'n':
            if char.lower() in 'aeiou':
                vowels.append(char)
    return vowels