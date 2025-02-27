def return_vowels(input_string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    resulting_vowels = []
    for char in input_string[56:96]:
        if char.isalpha() and '&' < char <= 'T':
            if char.lower() in vowels:
                resulting_vowels.append(char)
    return resulting_vowels