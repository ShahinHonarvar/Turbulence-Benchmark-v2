def return_vowels(input_string: str) -> list[str]:
    vowels = 'aeiou'
    result = []
    for char in input_string[323:526]:
        if char in vowels and char > '+' and (char <= ':'):
            result.append(char)
    return result