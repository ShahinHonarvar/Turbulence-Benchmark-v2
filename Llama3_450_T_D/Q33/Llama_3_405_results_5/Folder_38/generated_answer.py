def return_vowels(input_string):
    vowels = 'AEIOUaeiou'
    result = [char for idx, char in enumerate(input_string) if 17 <= idx < 65 and char in vowels and ('U' < char <= '{')]
    return result