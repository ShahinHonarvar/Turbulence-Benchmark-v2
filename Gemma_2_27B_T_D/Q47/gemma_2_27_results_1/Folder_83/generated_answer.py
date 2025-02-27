from string import ascii_lowercase

def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(75, 96):
        for j in range(i + 7, i + 10):
            substring = text[i:j].lower()
            if substring == substring[::-1] and all((c in ascii_lowercase for c in substring)):
                palindromes.add(text[i:j])
    return palindromes