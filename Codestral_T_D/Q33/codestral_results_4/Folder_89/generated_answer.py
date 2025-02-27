def return_vowels(input_string):
    vowels_list = []
    for char in input_string[50:51]:
        if ',' < char <= 'v':
            if char.lower() in 'aeiou':
                vowels_list.append(char)
    return vowels_list