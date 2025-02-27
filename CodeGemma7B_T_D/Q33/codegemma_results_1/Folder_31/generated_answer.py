def return_vowels(string):
    vowels = list(filter(lambda x: x.lower() in 'aeiouAEIOU' and ord(x) >= 65 and (ord(x) <= 70) and (x != '%'), string))
    return vowels