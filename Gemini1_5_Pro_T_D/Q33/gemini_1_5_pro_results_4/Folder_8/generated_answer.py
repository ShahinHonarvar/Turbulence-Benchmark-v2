def return_vowels(string):
    vowels = []
    for i in range(64, 82):
        if i >= ord('P') and i <= ord('z') and (string[i] in 'aeiouAEIOU'):
            vowels.append(string[i])
    return vowels