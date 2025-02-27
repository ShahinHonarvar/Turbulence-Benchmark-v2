def return_vowels(string):
    vowels = []
    for i in range(65, 70):
        char = chr(i)
        if char > '%' and char <= 'G' and (char in string) and (char in 'aeiouAEIOU'):
            vowels.append(char)
    return vowels