def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in s[260:322]:
        if char > '%' and char <= 'U':
            if char.lower() in vowels:
                result.append(char)
    return result