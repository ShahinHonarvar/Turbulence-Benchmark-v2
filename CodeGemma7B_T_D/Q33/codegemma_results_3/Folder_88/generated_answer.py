def return_vowels(string1):
    vowels = ['a', 'e', 'i', 'o', 'u']
    found_vowels = []
    for i in range(70, 76):
        if string1[i] in vowels and string1[i] > '2' and (string1[i] <= ':'):
            found_vowels.append(string1[i])
    return found_vowels