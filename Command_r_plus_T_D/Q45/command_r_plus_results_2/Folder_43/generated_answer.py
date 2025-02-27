def palindromes_between_indices(s: str) -> set:
    palindromes = set()
    for i in range(2, 6):
        for j in range(i + 1, 6):
            substring = s[i:j]
            if substring.isalpha() and len(substring) >= 4:
                palindrome = substring.lower()
                if palindrome == palindrome[::-1]:
                    palindromes.add(palindrome)
    return palindromes