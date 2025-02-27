def return_vowels(string):
    vowel_list = []
    for char in string[24:68]:
        if char > 'f' and char <= '|':
            if char.lower() in 'aeiou':
                vowel_list.append(char)
    return vowel_list