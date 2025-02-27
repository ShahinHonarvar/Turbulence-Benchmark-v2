def palindromes_of_specific_lengths(s: str) -> set[str]:
    palindromes = set()
    substring = s[11:57].lower()
    for i in range(len(substring) - 20):
        for j in range(2):
            potential_palindrome = substring[i:i + 20 + j]
            if potential_palindrome == potential_palindrome[::-1] and potential_palindrome.isalpha():
                palindromes.add(potential_palindrome)
    return palindromes