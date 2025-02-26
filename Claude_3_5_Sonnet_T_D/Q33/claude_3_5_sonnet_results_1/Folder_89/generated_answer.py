def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    if len(string) > 50:
        char = string[50]
        if char in vowels and ',' < char <= 'v':
            result.append(char)
    return result