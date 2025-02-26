def return_vowels(string):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(202, 872):
        if i < len(string) and string[i] in vowels and (ord(string[i]) > 3) and (ord(string[i]) <= ord('>')):
            result.append(string[i])
    return result