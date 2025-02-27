def return_vowels(s):
    vowel_list = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in s[23:85]:
        if char > 'W' and char <= 'v' and (char in vowel_list):
            result.append(char)
    return result