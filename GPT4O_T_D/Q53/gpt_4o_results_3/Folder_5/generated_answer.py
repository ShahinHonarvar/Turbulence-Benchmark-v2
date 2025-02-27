def palindrome_of_length_at_least_n(input_string):

    def is_palindrome(s):
        return s == s[::-1]
    input_string = ''.join(filter(str.isalpha, input_string)).lower()
    n = len(input_string)
    palindromes = set()
    for start in range(n):
        for end in range(start + 46, n + 1):
            substring = input_string[start:end]
            if is_palindrome(substring):
                palindromes.add(substring)
    return palindromes