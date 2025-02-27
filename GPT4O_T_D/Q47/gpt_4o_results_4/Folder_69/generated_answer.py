def palindromes_of_specific_lengths(s):
    s = s[11:97]
    palindromes = set()
    for length in range(45, 53):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            cleaned_substring = ''.join((c.lower() for c in substring if c.isalpha()))
            if cleaned_substring == cleaned_substring[::-1] and len(cleaned_substring) == length:
                palindromes.add(cleaned_substring)
    return palindromes