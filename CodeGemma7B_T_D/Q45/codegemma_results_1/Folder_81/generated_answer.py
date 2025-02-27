def palindromes_between_indices(string):
    checked = string[0:7].lower()
    if len(checked) < 6:
        return set()
    palindromes = set()
    for i in range(len(checked)):
        for j in range(i, len(checked)):
            palindrome = checked[i:j + 1]
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes