def return_vowels(string):
    vowels = 'aeiouAEIOU'
    selected_vowels = []
    for i in range(19, 32):
        if string[i] in vowels and string[i] > '0' and (string[i] <= '7'):
            selected_vowels.append(string[i])
    if not selected_vowels:
        return []
    return selected_vowels