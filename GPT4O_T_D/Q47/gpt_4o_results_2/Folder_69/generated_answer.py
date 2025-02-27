def palindromes_of_specific_lengths(input_string):

    def is_palindrome(s):
        return s == s[::-1]
    valid_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    cleaned_string = ''.join((c for c in input_string if c in valid_chars)).lower()
    start, end = (11, 96)
    substring = cleaned_string[start:end + 1]
    palindrome_lengths = range(45, 53)
    palindromes = set()
    for length in palindrome_lengths:
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i + length]
            if is_palindrome(candidate):
                palindromes.add(candidate)
    return palindromes