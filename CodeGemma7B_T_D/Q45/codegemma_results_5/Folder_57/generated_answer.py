def palindromes_between_indices(s):
    start = 2
    end = 5
    palindromes = set()
    for left in range(start, end + 1):
        for right in range(left, end + 1):
            substring = s[left:right + 1]
            if substring == substring[::-1]:
                palindromes.add(substring.lower())
    return palindromes