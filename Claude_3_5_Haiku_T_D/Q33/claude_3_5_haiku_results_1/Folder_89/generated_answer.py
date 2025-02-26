def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(50, 51):
        if i < len(string):
            char = string[i].lower()
            if char in vowels and ',' < char <= 'v':
                result.append(char)
    return result