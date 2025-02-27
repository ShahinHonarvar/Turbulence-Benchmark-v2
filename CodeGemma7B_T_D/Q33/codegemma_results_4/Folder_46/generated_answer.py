def return_vowels():
    vowels = []
    for i in range(10, 83):
        if 'a' <= str(i) <= 'z':
            vowels.append(chr(i))
    return vowels