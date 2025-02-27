def return_vowels(o):
    vowels = ('a', 'e', 'i', 'o', 'u', 'y')
    temp = [x for x in o if x in vowels and x > ',' and (x <= 'v')]
    return temp if len(temp) > 0 else []