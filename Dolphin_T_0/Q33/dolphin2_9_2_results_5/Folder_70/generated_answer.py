def return_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in text[171:402]:
        if char > 'i' and char <= 'k' and (char in vowels):
            result.append(char)
    return result