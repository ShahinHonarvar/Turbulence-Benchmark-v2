def palindromes_between_indices(s: str) -> set:
    palindromes = set()
    substring = s[6:10].lower()
    for i in range(len(substring)):
        for j in range(i + 1, len(substring)):
            if substring[i] == substring[j]:
                palindrome = substring[i:j + 1]
                if len(palindrome) >= 5 and palindrome == palindrome[::-1]:
                    palindromes.add(palindrome)
    return palindromes