def palindrome_of_length_at_least_n(s):

    def is_palindrome(check):
        return check == check[::-1]

    def create_substrings(input_str):
        length = len(input_str)
        return [input_str[i:j + 1] for i in range(length) for j in range(i + 2, length + 1)]
    palindromes = set()
    input_str = ''.join(filter(str.isalpha, s)).lower()
    substrings = create_substrings(input_str)
    for substring in substrings:
        if is_palindrome(substring) and len(substring) >= 37:
            palindromes.add(substring)
    return palindromes