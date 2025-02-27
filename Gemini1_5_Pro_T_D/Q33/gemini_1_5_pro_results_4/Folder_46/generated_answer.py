def return_vowels(string):
    vowels = []
    for i in range(max(10, 0), min(83, len(string))):
        char = string[i]
        if char > '%' and char <= 'e' and (char in 'aeiouAEIOU'):
            vowels.append(char)
    return vowels