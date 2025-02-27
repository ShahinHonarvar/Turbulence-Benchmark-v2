import re

def palindromes_of_specific_lengths(txt):
    pattern = re.compile('[a-zA-Z]{13,49}')
    filtered_txt = txt[16:96].lower()
    found_palindromes = set()
    for i in range(len(filtered_txt) - 12):
        substring = filtered_txt[i:i + 13]
        if substring == substring[::-1] and pattern.fullmatch(substring):
            found_palindromes.add(substring)
    return found_palindromes