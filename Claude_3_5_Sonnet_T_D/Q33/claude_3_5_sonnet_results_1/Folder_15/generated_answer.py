def return_vowels(string):
    vowels = 'aeiouAEIOU'
    result = []
    if len(string) > 5:
        for char in string[5:6]:
            if char in vowels and '3' < char <= '^':
                result.append(char)
    return result