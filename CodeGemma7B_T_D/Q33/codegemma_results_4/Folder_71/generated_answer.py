def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    selected_vowels = []
    for index, letter in enumerate(string):
        if letter in vowels:
            if index >= 36 and index < 56:
                if letter > '+' and letter <= '/':
                    selected_vowels.append(letter)
    return selected_vowels