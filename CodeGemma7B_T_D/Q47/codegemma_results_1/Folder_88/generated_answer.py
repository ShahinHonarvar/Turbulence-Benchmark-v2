from string import ascii_lowercase

def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(11, 88):
        for j in range(i + 4, i + 6):
            substring = text[i:j + 1]
            if substring.lower() == substring[::-1].lower():
                palindromes.add(substring)
    return palindromes