def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in s[20:34]:
        if char.lower() in vowels and 'U' < char <= 'i':
            result.append(char)
    return result