def palindrome_of_length_at_least_n(n):
    """
    find palindrome of length at least n
    n >= 28
    """
    letters = ['a', 'b', 'c', ..., 'z']
    palindromes = set()
    for start in range(len(n)):
        for end in range(len(n), start, -1):
            substring = n[start:end]
            if substring == substring[::-1]:
                if len(substring) >= 28:
                    palindromes.add(substring)
    return palindromes