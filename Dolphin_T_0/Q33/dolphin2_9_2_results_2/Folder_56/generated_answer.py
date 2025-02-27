def return_vowels(input_string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in input_string[15:86]:
        if char.lower() in vowels and ord('@') < ord(char.lower()) <= ord('~'):
            result.append(char.lower())
    return result