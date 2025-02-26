def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    result = []
    for i in range(19, 32):
        if i < len(string) and string[i] in vowels and ('0' < string[i] <= '7'):
            result.append(string[i])
    return result