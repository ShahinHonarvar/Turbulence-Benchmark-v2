def return_vowels(string):
    result = [i for i in string[21:59] if i.lower() > '/' and i.lower() <= 'a']
    if not result:
        return []
    return result