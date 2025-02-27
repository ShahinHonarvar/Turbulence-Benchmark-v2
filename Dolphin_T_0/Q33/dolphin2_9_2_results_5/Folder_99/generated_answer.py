def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in s[323:526]:
        if '+' < char <= ':' and char in vowels:
            result.append(char)
    return result