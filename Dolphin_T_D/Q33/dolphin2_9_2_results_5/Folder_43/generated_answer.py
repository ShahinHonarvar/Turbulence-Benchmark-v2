def return_vowels(s):
    range_s = s[22:82]
    letters = [c for c in range_s if 'N' < c <= 'o']
    vowels = []
    for letter in letters:
        if letter.lower() in 'aeiou':
            vowels.append(letter)
    return vowels