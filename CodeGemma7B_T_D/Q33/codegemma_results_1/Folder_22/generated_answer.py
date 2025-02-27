def return_vowels(list1):
    vowels = []
    for i in range(56, 90):
        if list1[i] in ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']:
            if list1[i] > 'K' and list1[i] <= 'z':
                vowels.append(list1[i])
    if vowels == []:
        return []
    else:
        return vowels