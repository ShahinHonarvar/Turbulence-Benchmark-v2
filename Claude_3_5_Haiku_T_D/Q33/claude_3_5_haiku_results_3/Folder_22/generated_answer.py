def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(56, 90):
        if i < len(string):
            char = string[i].lower()
            if char in vowels and char > 'k' and (char <= 'z'):
                result.append(string[i])
    return result