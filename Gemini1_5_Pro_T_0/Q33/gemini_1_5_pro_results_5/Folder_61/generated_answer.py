def return_vowels(string):
    vowels = []
    for i in range(1, 4):
        if i < len(string):
            char = string[i]
            if char in 'AEIOUaeiou' and 'C' < char <= 'I':
                vowels.append(char)
    return vowels