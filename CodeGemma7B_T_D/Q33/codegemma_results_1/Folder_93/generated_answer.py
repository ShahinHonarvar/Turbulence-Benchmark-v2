def return_vowels(str):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(54, 82):
        if str[i] in vowels and ord(str[i]) <= ord('@') and (ord(str[i]) >= ord('=') - 27):
            result.append(str[i])
    return result