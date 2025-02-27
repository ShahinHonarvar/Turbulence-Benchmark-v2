def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    filtered_vowels = []
    for i in range(10, 82):
        if string[i] in vowels and ord(string[i]) > ord('$') and (ord(string[i]) <= ord('@')):
            filtered_vowels.append(string[i])
    return filtered_vowels