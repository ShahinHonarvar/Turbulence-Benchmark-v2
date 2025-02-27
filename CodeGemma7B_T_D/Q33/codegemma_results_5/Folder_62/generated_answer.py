def return_vowels(str):
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowels_result = list(filter(lambda i: i in vowels and 14 <= i <= 59 and (ord(str[i]) > ord('D') and ord(str[i]) <= ord('v')), range(len(str))))
    if vowels_result:
        return list(map(lambda i: str[i], vowels_result))
    else:
        return []