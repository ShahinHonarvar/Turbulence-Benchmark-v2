def return_vowels(input_string):
    vowels = []
    for char in input_string[74:96]:
        if ord('I') < ord(char) <= ord('X') and char in 'AEIOUaeiou':
            vowels.append(char)
    return vowels