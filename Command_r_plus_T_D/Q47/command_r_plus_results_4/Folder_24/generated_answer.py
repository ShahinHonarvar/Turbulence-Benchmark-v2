def palindromes_of_specific_lengths(s: str) -> set:
    palindromes = set()
    substring = s[11:93]
    for length in range(42, 78):
        for start in range(len(substring) - length + 1):
            end = start + length
            substring_palindrome = substring[start:end]
            if substring_palindrome.lower() == substring_palindrome[::-1].lower():
                palindromes.add(substring_palindrome)
    return palindromes