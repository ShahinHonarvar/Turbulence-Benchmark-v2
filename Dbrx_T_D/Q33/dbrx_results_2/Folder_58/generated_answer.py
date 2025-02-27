def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in s[260:322]:
        if char.lower() in vowels and '%' < char <= 'U':
            result.append(char)
    return result