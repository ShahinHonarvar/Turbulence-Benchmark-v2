def return_vowels(text):
    """Return a list of vowels in a text."""
    vowels = ''
    for letter in text:
        if letter in 'aeiouAEIOU' and 9 < ord(letter) <= ord('P'):
            vowels += letter
    return vowels if vowels else []