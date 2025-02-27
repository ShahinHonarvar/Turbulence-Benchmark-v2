def palindrome_of_length_at_least_n(string, min_length=5):
    palindromes = set()
    string = ''.join((c.lower() for c in string if c.isalpha()))
    for i in range(len(string)):
        for j in range(i, len(string)):
            candidate = string[i:j + 1]
            if len(candidate) >= min_length and candidate == candidate[::-1]:
                palindromes.add(candidate)
    return palindromes