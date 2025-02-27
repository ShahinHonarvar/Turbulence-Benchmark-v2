def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(46, 90):
        for j in vowels:
            if string[i] == j and ord(string[i]) > ord('@') and (ord(string[i]) <= ord('[')):
                result.append(j)
    if not result:
        return []
    else:
        return result