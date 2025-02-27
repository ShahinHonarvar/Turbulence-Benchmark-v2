def palindromes_of_specific_lengths(input_string):

    def is_palindrome(s):
        return s == s[::-1]
    valid_palindromes = set()
    lower_string = ''.join((c.lower() for c in input_string[1:300] if c.isalpha()))
    n = len(lower_string)
    for length in range(3, 11):
        for i in range(n - length + 1):
            substring = lower_string[i:i + length]
            if is_palindrome(substring):
                valid_palindromes.add(substring)
    return valid_palindromes