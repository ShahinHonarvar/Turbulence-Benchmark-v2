def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in s[43:70]:
        if '*' < char <= 'b' and char in vowels:
            result.append(char)
    return result