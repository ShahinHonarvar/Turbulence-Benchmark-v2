def return_vowels(string):
    result = [i for i in string[32:97] if i in ['A', 'E', 'I', 'O', 'U'] and ord('Q') < ord(i) <= ord(']')]
    return result