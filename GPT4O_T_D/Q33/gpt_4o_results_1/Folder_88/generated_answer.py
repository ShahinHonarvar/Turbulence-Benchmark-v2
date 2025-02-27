def return_vowels(input_string):
    vowels = 'AEIOUaeiou'
    result = []
    for char in input_string[70:76]:
        if char in vowels and '2' < char <= ':':
            result.append(char)
    return result