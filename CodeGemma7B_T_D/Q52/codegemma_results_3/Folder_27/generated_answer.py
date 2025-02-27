import re

def palindrome_of_length_n(txt):
    results = set()
    txt = txt.lower()
    palindromes_of_length_n = re.findall('(?i)(\\\\w{56})\\\\1', txt, re.IGNORECASE)
    if len(palindromes_of_length_n) == 0:
        return results
    for palindrome in palindromes_of_length_n:
        results.add(palindrome)
    return results