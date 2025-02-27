from string import ascii_lowercase

def palindromes_of_specific_lengths(text):
    lowercased_text = text.lower()
    palindromes = set()
    for i in range(35, 89):
        for j in range(24, 34):
            substring = lowercased_text[i - j:i + 1]
            if substring == substring[::-1] and all((char in ascii_lowercase for char in substring)):
                palindromes.add(substring)
    return palindromes