def palindrome_of_length_at_least_n(input_string):

    def is_palindrome(s):
        return s == s[::-1]
    input_string = ''.join(filter(str.isalpha, input_string.lower()))
    palindromes = set()
    for i in range(len(input_string)):
        for j in range(i + 57, len(input_string) + 1):
            substring = input_string[i:j]
            if is_palindrome(substring):
                palindromes.add(substring)
    return palindromes