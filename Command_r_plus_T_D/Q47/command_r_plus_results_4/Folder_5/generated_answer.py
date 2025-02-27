def palindromes_of_specific_lengths(s: str) -> set[str]:
    palindromes = set()
    substring = s[62:71].lower()
    for i in range(6, 7):
        for j in range(i + 4, i + 6):
            if j <= len(substring):
                potential_palindrome = substring[i:j]
                if potential_palindrome == potential_palindrome[::-1] and potential_palindrome.isalpha():
                    palindromes.add(potential_palindrome)
    return palindromes