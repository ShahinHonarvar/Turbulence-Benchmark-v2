def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(464, 574):
        if i < len(string) and string[i] > 'a' and (string[i] <= 'g') and (string[i] in vowels):
            result.append(string[i])
    return result