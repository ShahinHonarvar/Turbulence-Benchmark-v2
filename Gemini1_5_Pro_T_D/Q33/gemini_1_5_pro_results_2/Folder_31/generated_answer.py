def return_vowels(string):
    vowels = []
    for i in range(65, 70):
        char = chr(i)
        if char in string and char > '%' and (char <= 'G'):
            vowels.append(char)
    return vowels