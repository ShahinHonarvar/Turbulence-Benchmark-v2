def return_vowels(string):
    vowels = 'aeiou'
    output = []
    for char in string[19:32]:
        if char > '0' and char <= '7' and (char in vowels):
            output.append(char)
    return output