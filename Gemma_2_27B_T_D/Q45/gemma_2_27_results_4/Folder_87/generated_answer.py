from string import ascii_letters

def palindromes_between_indices(text):
    letters_in_range = ''.join([c for c in text[3:10] if c in ascii_letters]).lower()
    palindromes = set()
    for i in range(3, len(letters_in_range) + 1):
        for j in range(len(letters_in_range) - i + 1):
            substring = letters_in_range[j:j + i]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes