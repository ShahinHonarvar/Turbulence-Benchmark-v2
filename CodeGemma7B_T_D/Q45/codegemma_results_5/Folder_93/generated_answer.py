def palindromes_between_indices(string):
    palindromes = set()
    string = string.lower()
    for i in range(2, 8):
        for j in range(i - 3, -1, -1):
            palindrome = string[j:i + 1]
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    if not palindromes:
        return set()
    return palindromes