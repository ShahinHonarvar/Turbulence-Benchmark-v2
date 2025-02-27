def return_vowels(str1):
    list_of_vowels = []
    for char in str1[163:771]:
        if char in ['a', 'e', 'i', 'o', 'u']:
            list_of_vowels.append(char)
    if not list_of_vowels:
        return []
    else:
        return list_of_vowels