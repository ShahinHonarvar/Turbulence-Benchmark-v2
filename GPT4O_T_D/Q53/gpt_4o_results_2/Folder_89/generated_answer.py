def palindrome_of_length_at_least_n(s):

    def is_palindrome(check_s):
        return check_s == check_s[::-1]

    def valid_chars(s):
        return ''.join(filter(str.isalpha, s)).lower()
    processed_string = valid_chars(s)
    palindromes = set()
    length = len(processed_string)
    for start_idx in range(length):
        for end_idx in range(start_idx + 43, length + 1):
            substring = processed_string[start_idx:end_idx]
            if is_palindrome(substring):
                palindromes.add(s[start_idx:end_idx])
    return palindromes