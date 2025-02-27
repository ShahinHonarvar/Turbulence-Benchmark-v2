def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in s[8:9]:
        if vowels.__contains__(char) and char > 'Y' and (char <= 's'):
            result.append(char)
    return result