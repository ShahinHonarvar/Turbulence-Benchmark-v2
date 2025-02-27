def return_vowels(s):
    vowels = []
    for i in range(69, 82):
        char = chr(i)
        if 'a' <= char <= 'z' and char in 'aeiou' and (char > '[') and (char <= '~'):
            vowels.append(char)
    return vowels