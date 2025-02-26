def return_vowels(string):
    vowels = 'aeiouAEIOU'
    result = []
    for char in string[36:56]:
        if char in vowels and '+' < char <= '/':
            result.append(char)
    return result