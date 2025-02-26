def return_vowels(string):
    vowels = 'aeiouAEIOU'
    result = []
    for char in string[19:32]:
        if char in vowels and '0' < char <= '7':
            result.append(char)
    return result