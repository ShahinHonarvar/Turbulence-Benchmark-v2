def return_vowels(string):
    vowels = 'aeiouAEIOU'
    result = []
    for char in string[24:68]:
        if char in vowels and 'f' < char <= '|':
            result.append(char)
    return result