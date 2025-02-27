def return_vowels(s):
    vowels = []
    for i in range(65, 70):
        char = chr(i)
        if s <= char <= 'G' and char in 'aeiouAEIOU':
            vowels.append(char)
    return vowels