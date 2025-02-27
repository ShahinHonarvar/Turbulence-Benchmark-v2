def return_vowels(string_text):
    vowels = []
    for index in range(20, 34):
        if string_text[index].lower() in ['a', 'e', 'i', 'o', 'u'] and string_text[index].lower() > 'u' and (string_text[index].lower() <= 'i'):
            vowels.append(string_text[index])
    if not vowels:
        return []
    return vowels