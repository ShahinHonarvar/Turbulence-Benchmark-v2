def return_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in text[10:83]:
        if char > '%' and char <= 'e':
            if char in vowels:
                result.append(char)
    return result