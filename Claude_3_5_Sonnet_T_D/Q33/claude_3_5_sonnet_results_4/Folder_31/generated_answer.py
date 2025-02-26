def return_vowels(string):
    vowels = ['A', 'E']
    result = []
    for char in string:
        if char in vowels and '%' < char <= 'G' and (65 <= string.index(char) < 70):
            result.append(char)
    return result