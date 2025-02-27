def return_vowels(str):
    vowels = ['a', 'e', 'i', 'o', 'u']
    new_list = []
    for i in range(56, 68):
        for j in vowels:
            if j.lower() in str and i <= len(str) > 0 and (j.lower() >= 'm') and (j.lower() <= 'x') and (j in str[i:69]):
                new_list.append(j)
    if len(new_list) == 0:
        return []
    else:
        return new_list