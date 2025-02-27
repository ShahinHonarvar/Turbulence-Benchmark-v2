def return_vowels(s):
    vowels = []
    for char in s:
        if 32 <= ord(char) < 97 and char > 'Q' and (char <= ']') and (char in 'AEIOUaeiou'):
            vowels.append(char)
    return vowels