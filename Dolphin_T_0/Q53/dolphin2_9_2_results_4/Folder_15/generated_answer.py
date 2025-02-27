def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    for length in range(len(s), 3, -1):
        for start_index in range(len(s) - length + 1):
            substr = s[start_index:start_index + length]
            if substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes