def palindromes_of_specific_lengths(s):

    def is_palindrome(substr):
        filtered_chars = ''.join(filter(str.isalpha, substr)).lower()
        return filtered_chars == filtered_chars[::-1]
    palindromes = set()
    start, end = (13, 99)
    for length in range(26, 30):
        for i in range(start, end - length + 2):
            substring = s[i:i + length]
            if is_palindrome(substring):
                palindromes.add(substring)
    return palindromes