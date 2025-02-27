def return_vowels(string):
    vowels = []
    for i in range(23, 75):
        ch = string[i]
        if ch in 'aeiouAEIOU' and ord(ch) > ord('L') and (ord(ch) <= ord('d')):
            vowels.append(ch)
    return vowels