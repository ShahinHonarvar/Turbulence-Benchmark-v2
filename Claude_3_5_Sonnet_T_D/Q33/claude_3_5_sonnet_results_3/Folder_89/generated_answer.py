def return_vowels(input_string):
    vowels = 'aeiouAEIOU'
    result = []
    if len(input_string) > 50:
        for char in input_string[50:51]:
            if char in vowels and ',' < char <= 'v':
                result.append(char)
    return result