def return_vowels(text):
    first = 50
    last = 77
    vowels = ['a', 'e', 'i', 'o', 'u']
    return_list = []
    for i in range(first, last):
        if text[i] not in vowels and text[i] > '#':
            for j in vowels:
                if j == text[i].lower():
                    return_list.append(j)
    return return_list