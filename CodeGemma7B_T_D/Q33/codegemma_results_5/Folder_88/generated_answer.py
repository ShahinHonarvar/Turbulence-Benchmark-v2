def return_vowels(a_string):
    vowels = []
    for i in range(70, 76):
        if a_string[i] in 'AEIOUaeiou':
            if ord(a_string[i]) > 2 and ord(a_string[i]) <= ord('.'):
                vowels.append(a_string[i])
    return vowels