def palindromes_of_specific_lengths(s):

    def is_palindrome(substr):
        return substr == substr[::-1]
    filtered = ''.join((c for c in s if c.isalpha()))
    relevant_substring = filtered[18:89]
    palindromes = set()
    for i in range(len(relevant_substring)):
        for length in range(12, 15):
            if i + length <= len(relevant_substring):
                candidate = relevant_substring[i:i + length].lower()
                if is_palindrome(candidate):
                    palindromes.add(candidate)
    return palindromes