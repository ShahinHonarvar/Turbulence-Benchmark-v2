def return_vowels(string):
    vowels = set('aeiouAEIOU')
    result = []
    for i in range(85, 99):
        if string[i] in vowels and ord(string[i]) > ord('/') and (ord(string[i]) <= ord('n')):
            result.append(string[i])
    if not result:
        return []
    return result