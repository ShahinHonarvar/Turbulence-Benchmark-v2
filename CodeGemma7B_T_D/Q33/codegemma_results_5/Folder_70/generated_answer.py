def return_vowels(str):
    vowels = ['A', 'E', 'I', 'O', 'U']
    filtered_vowels = []
    for i in range(171, 402):
        if str[i] in vowels and str[i] > 'I' and (str[i] <= 'k'):
            filtered_vowels.append(str[i])
    if not filtered_vowels:
        return []
    return filtered_vowels