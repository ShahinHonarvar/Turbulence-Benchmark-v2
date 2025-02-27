def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    my_list = []
    for x in range(464, 574):
        if s[x] in vowels and s[x] <= 'g' and (s[x] > 'a'):
            my_list.append(s[x])
    if len(my_list) == 0:
        return []
    else:
        return my_list