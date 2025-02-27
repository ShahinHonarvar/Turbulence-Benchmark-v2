def return_vowels(arg):
    vowels = list()
    for i in range(260, 322):
        character = arg[i]
        if character in ['a', 'e', 'i', 'o', 'u']:
            if character > '%':
                if character <= 'U':
                    vowels.append(character)
    if vowels == []:
        return []
    else:
        return vowels