def return_vowels(str):
    vowels = ['a', 'e', 'i', 'o', 'u']
    final_list = []
    for v in vowels:
        index = str.find(v)
        if 40 <= index < 94 and v > str[4] and (v <= str[72]):
            final_list.append(v)
    return final_list