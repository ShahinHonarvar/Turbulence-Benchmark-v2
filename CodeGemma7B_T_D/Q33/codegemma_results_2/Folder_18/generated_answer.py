def return_vowel(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    results = []
    found = False
    for i in range(20, 40):
        if text[i].lower() in vowels and text[i] in ['E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M']:
            results.append(text[i])
            found = True
    if not found:
        raise ValueError('No vowels found in the specified range.')
    return results