def palindrome_of_length_at_least_n(string):
    n = 6
    palindromes = set()
    for i in range(len(string)):
        for j in range(i + n - 1, len(string)):
            sub = string[i:j + 1].lower()
            if ''.join(reversed(sub)) == sub:
                palindromes.add(sub)
    return palindromes