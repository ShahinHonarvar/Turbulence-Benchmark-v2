def palindromes_of_specific_lengths(s):

    def is_palindrome(substr):
        return substr == substr[::-1]
    start, end = (11, 83)
    min_len, max_len = (37, 60)
    filtered_substring = ''.join((c for c in s[start:end + 1] if c.isalpha())).lower()
    palindromes = set()
    for length in range(min_len, max_len + 1):
        for i in range(len(filtered_substring) - length + 1):
            candidate = filtered_substring[i:i + length]
            if is_palindrome(candidate):
                palindromes.add(candidate)
    return palindromes