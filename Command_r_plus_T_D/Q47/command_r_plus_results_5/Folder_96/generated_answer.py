def palindromes_of_specific_lengths(s: str) -> set:
    palindromes = set()
    substring = s[99:301].lower()
    for i in range(100, 251):
        for j in range(i + 50, 301):
            potential_palindrome = substring[j - i:j]
            if potential_palindrome == potential_palindrome[::-1] and potential_palindrome.isalpha():
                palindromes.add(potential_palindrome)
    return palindromes