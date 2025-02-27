def return_vowels(s):
    vowels = []
    for char in s:
        if ord('P') < ord(char) <= ord('z') and 64 <= ord(char) <= 82:
            vowels.append(char)
    return vowels