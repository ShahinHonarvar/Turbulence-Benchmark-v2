def return_vowels():
    string = input()
    vowels = ['a', 'e', 'i', 'o', 'u']
    newlist1 = list()
    for i in range(23, 85):
        if string[i] in vowels and ord(string[i]) > ord('W') and (ord(string[i]) <= ord('v')):
            newlist1.append(string[i])
    if len(newlist1) == 0:
        return []
    else:
        return newlist1