def return_vowels(str1):
    vowel = ['a', 'e', 'i', 'o', 'u']
    str2 = str1[44:95]
    list1 = []
    for i in str2:
        if i in vowel and ord(i) > 5 and (ord(i) <= ord('<')):
            list1.append(i)
    if not list1:
        return []
    else:
        return list1