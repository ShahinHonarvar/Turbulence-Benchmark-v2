def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(323, 526):
        if string[i] > '+' and string[i] <= ':' and (string[i] in vowels):
            result.append(string[i])
    return result