def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = []
    for char in s[641:872]:
        if '>' < char <= 'q' and char in vowels:
            result.append(char)
    return result