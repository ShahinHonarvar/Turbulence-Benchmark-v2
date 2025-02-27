def return_vowels(s):
    new_list = [x for x in s if x.lower() in 'aeiou' and 1 <= s.index(x) <= 7 and (x.lower() > 'f') and (x.lower() <= 'j')]
    return new_list if new_list else []