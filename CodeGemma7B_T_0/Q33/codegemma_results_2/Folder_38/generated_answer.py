def return_vowels(string):
    vowels = []
    for i in range(17, 65):
        if string[i].lower() in 'aeiouAEIOU' and string[i] > 'U' and (string[i] <= '{'):
            vowels.append(string[i])
    return vowels