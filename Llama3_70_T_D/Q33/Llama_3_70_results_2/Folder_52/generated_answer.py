def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = []
    for char in s[24:68]:
        if vowels.find(char) != -1 and 'f' < char <= '|':
            result.append(char)
    return result