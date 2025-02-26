def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    result = []
    for idx, char in enumerate(string):
        if 71 <= idx < 81 and char in vowels and (char > '>') and (char <= 'U'):
            result.append(char)
    return result