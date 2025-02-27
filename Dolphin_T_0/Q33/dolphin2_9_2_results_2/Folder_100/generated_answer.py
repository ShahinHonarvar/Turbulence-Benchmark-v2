def return_vowels(input_string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    selected_vowels = []
    for char in input_string[23:75]:
        if 'L' < char <= 'd' and char in vowels:
            selected_vowels.append(char)
    return selected_vowels