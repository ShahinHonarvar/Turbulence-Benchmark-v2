def return_vowels(s):
    vowels = []
    for i in range(40, 94):
        char = s[i]
        if char > chr(4) and char <= 'H' and (char in 'AEIOUaeiou'):
            vowels.append(char)
    return vowels