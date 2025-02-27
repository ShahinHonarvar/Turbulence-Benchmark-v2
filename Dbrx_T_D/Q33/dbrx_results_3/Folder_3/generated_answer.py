def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(50, 77):
        if i >= len(s):
            break
        char = s[i]
        if char > '#' and char <= 'r' and (char in vowels):
            result.append(char)
    return result