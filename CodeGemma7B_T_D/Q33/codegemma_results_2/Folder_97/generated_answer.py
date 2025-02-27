def return_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    filtered_vowels = []
    if 328 <= len(text) < 455:
        for i in range(328, 455):
            if text[i].lower() in vowels and text[i] <= 'z' and (text[i] > '<'):
                filtered_vowels.append(text[i])
    return filtered_vowels