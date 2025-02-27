def return_vowels(input_string):
    vowels = []
    for char in input_string[170:645]:
        if char > 'E' and char <= '~':
            if char.lower() in 'aeiou':
                vowels.append(char)
    return vowels