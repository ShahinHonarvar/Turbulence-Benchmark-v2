import re

def palindromes_between_indices(text):
    matches = re.findall('([a-zA-Z]+)', text[2:9])
    palindromes = set()
    for i in range(len(matches) - 5):
        for j in range(i + 6, len(matches)):
            palindrome = ''.join(sorted(matches[i:j + 1], key=str.upper))
            palindromes.add(palindrome)
    return palindromes