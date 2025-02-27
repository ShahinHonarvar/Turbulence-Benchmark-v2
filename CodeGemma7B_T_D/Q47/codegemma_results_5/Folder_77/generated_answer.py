from string import ascii_lowercase

def palindromes_of_specific_lengths(text):
    palindromes = set()
    for start in range(103, 277):
        for end in range(start + 100, start + 170):
            substring = text[start:end].lower()
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes