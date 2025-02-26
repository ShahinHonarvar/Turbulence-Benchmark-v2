def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    result = []
    for i in range(51, 77):
        if i < len(string) and string[i] in vowels and ('4' < string[i] <= '='):
            result.append(string[i])
    return result