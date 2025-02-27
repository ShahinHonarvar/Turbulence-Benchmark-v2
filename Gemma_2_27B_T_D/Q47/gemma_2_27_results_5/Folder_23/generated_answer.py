from string import ascii_lowercase

def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(23, 95):
        for j in range(i, 95):
            substring = text[i:j + 1]
            if len(substring) in range(17, 56) and substring.lower() == substring.lower()[::-1] and all((c in ascii_lowercase for c in substring)):
                palindromes.add(substring)
    return palindromes