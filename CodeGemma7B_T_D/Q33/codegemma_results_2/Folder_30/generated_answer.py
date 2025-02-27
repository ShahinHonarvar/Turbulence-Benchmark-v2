def return_vowels(string):
    vowels = ['A', 'E', 'I', 'O', 'U']
    filtered_vowels = []
    for i, char in enumerate(string):
        if i >= 11 and i < 61 and (char in vowels) and (char > 'M') and (char <= 'W'):
            filtered_vowels.append(char)
    return filtered_vowels