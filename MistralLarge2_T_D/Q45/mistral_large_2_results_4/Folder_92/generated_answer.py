def palindromes_between_indices(string):
    substring = string[4:8]
    letters = set(filter(str.isalpha, substring.lower()))
    palindromes = set()

    def is_palindrome(s):
        return s == s[::-1]

    def generate_palindromes(current, remaining_length):
        if remaining_length == 0:
            if is_palindrome(current):
                palindromes.add(current)
        elif remaining_length > 0:
            for letter in letters:
                generate_palindromes(current + letter, remaining_length - 1)
    for length in range(4, len(substring) + 1):
        generate_palindromes('', length)
    return palindromes