def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for letter in s[44:95]:
        if letter in vowels and 5 < letter <= 9:
            result.append(letter)
    return result