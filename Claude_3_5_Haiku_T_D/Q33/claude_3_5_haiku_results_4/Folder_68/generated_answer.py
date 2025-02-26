def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for idx in range(1, 9):
        if idx < len(string):
            char = string[idx].lower()
            if char in vowels and '?' < char <= 'k':
                result.append(char)
    return result