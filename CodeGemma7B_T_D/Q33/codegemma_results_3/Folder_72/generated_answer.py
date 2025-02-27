def return_vowels(string):
    vowels = ['A', 'E', 'I', 'O', 'U']
    filtered_vowels = []
    for vowel in vowels:
        if string.find(vowel) in range(37, 57) and string[string.find(vowel)] > '*' and (string[string.find(vowel)] <= 'P'):
            filtered_vowels.append(vowel)
    return filtered_vowels