def remove_vowels(sentence):
    vowels = 'aeiouAEIOU'
    result = ''
    for letter in sentence:
        if letter not in vowels:
            result += letter
    return result