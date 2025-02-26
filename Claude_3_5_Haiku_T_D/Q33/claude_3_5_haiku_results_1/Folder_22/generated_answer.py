def return_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(56, 90):
        if i < len(text):
            char = text[i].lower()
            if char in vowels and 'k' < char <= 'z':
                result.append(text[i])
    return result