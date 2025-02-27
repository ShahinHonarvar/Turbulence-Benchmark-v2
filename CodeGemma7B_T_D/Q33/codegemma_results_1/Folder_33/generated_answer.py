def return_vowels(a):
    list = [x for x in a[163:771] if x.lower() in 'aeiou' and x > ':' and (x <= 'E')]
    return list if list else []