def palindromes_of_specific_lengths(s: str) -> set:
    palindromes = set()
    substring = s[63:71].lower()
    for i in range(6, 11):
        for j in range(i - 4, i + 1):
            potential_palindrome = substring[j:i]
            if potential_palindrome == potential_palindrome[::-1] and potential_palindrome.isalpha():
                palindromes.add(potential_palindrome)
    return palindromes