def return_vowels(str):
    cons_list = []
    vowels = 'aeiouAEIOU'
    for i in range(23, 57):
        if str[i] in vowels and str[i] != '0' and (str[i] <= 'd'):
            cons_list.append(str[i])
    if not cons_list:
        return []
    return cons_list