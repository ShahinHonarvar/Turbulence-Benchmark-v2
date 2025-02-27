def palindromes_of_specific_lengths(s: str) -> str:
    s = s[18:66]
    result = set()
    for i in range(len(s) - 22):
        for j in range(i + 23, len(s) + 1, 2):
            palindrome = s[i:j].lower()
            if palindrome == palindrome[::-1] and all((c.isalpha() for c in palindrome)):
                result.add(palindrome)
    return result