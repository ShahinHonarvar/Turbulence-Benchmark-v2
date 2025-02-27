def return_vowels(a_string):
    vowel_list = []
    for a_char in a_string[13:35]:
        if a_char > '8' and a_char <= 'F':
            vowel_list.append(a_char)
    return vowel_list