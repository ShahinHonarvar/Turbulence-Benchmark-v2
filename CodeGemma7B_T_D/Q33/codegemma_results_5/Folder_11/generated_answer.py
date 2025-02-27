def return_vowels(text):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    vowels_list = []
    for i in range(29, 73):
        if text[i] in vowels and text[i] > '#' and (text[i] <= '.'):
            vowels_list.append(text[i])
    return vowels_list