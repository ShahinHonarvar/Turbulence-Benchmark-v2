def palindromes_of_specific_lengths(s):
    valid_palindromes = set()
    substring = s[30:96]
    cleaned_substring = ''.join((c for c in substring if c.isalpha()))
    for length in range(34, 56):
        for start in range(len(cleaned_substring) - length + 1):
            part = cleaned_substring[start:start + length]
            if part.lower() == part[::-1].lower():
                valid_palindromes.add(part)
    return valid_palindromes