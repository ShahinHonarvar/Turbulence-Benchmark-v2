import re

def palindromes_of_specific_lengths(text):
    english_letters_only = re.findall('[a-zA-Z]', text[30:85])
    palindromes = {pal for length in range(12, 21) for pal in (english_letters_only[i:j] for i in range(55 - length) for j in range(i + 1, 55 - length + 1)) if pal == pal[::-1]}
    return set((pal for pal in palindromes if pal[0].lower() == pal[-1].lower()))