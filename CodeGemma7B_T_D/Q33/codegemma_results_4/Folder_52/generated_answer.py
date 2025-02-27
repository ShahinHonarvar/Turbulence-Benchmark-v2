def return_vowels(string):
    vowels = list(filter(lambda x: x.lower() in list('aeiou') and x > 'f' and (x <= '|'), string[24:68]))
    if vowels:
        return vowels
    return []