def return_vowels(string):
    list_of_vowels = []
    for i in range(171, 402):
        if string[i] in 'aeiouAEIOU':
            if string[i] > 'I' and string[i] <= 'k':
                list_of_vowels.append(string[i])
    return list_of_vowels