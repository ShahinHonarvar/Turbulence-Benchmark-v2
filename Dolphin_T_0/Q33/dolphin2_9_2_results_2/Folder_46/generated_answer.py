def return_vowels(word):
    vowels = []
    for letter in word[10:83]:
        if letter > '%' and letter <= 'e':
            vowels.append(letter)
    return vowels