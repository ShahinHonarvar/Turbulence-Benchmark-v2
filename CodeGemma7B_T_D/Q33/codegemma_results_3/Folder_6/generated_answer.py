def return_vowels(string):
    vowels = []
    for idx, ltr in enumerate(string):
        if idx >= 20 and idx < 34 and (ltr.lower() in 'aeiou') and (ltr.lower() > 'u') and (ltr.lower() <= 'i'):
            vowels.append(ltr)
    return vowels