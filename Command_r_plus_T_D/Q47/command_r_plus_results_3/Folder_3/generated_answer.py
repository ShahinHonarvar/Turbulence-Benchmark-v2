def palindromes_of_specific_lengths(s: str) -> set[str]:
    substring = s[26:96]
    palindromes = set()
    for i in range(len(substring) - 49):
        for j in range(3):
            potential_palindrome = substring[i:i + 49 + j]
            if potential_palindrome == potential_palindrome[::-1] and potential_palindrome.isalpha():
                palindromes.add(potential_palindrome)
    return palindromes