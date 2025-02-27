def return_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    index_260_322 = text[260:322]
    output = []
    for character in index_260_322:
        if (character > '%' and character <= 'U') and character in vowels:
            output.append(character)
    return output