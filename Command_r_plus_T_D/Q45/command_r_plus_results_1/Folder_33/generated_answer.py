def palindromes_between_indices(s: str) -> set:
    palindromes = set()
    substring = s[7:10].lower()
    for i in range(len(substring)):
        for j in range(i + 3, len(substring) + 1):
            palindrome = substring[i:j]
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes