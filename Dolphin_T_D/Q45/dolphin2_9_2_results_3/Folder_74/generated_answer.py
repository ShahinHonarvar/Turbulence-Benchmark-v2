def palindromes_between_indices(s: str) -> set:
    palindromes = set()
    for i in range(1, 6):
        for j in range(i + 2, len(s) + 1):
            substring = s[i:j]
            if len(substring) >= 6:
                palindrome = ''.join(sorted(substring.lower()))
                if palindrome == palindrome[::-1]:
                    palindromes.add(palindrome)
    return palindromes