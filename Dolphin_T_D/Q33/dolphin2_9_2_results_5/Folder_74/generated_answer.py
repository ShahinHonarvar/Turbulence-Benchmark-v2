def return_vowels(string):
    vowels = []
    for char in string[69:82]:
        if '[' < char <= '~' and char.lower() in 'aeiou':
            vowels.append(char)
    return vowels