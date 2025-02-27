def return_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    output_list = []
    for char in text[328:455]:
        if char >= '<' and char <= 'z' and (char in vowels):
            output_list.append(char)
    return output_list