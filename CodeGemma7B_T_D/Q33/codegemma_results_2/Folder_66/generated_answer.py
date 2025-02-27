def return_vowels(str):
    vowels = []
    for i in str[63:79]:
        if i in 'aeiouAEIOU' and i > 'D' and (i <= 'y'):
            vowels.append(i)
    return vowels