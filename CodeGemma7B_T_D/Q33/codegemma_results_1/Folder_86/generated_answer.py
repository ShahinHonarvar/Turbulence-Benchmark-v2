def return_vowels(str):
    vowels = 'aeiouAEIOU'
    vowels_list = []
    for i, char in enumerate(str):
        if char in vowels and i >= 273 and (i < 275) and (char > '+') and (char <= 'o'):
            vowels_list.append(char)
    if not vowels_list:
        return []
    else:
        return vowels_list