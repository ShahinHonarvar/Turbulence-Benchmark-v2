def palindrome_of_length_at_least_n(s):

    def is_palindrome(substr):
        return substr == substr[::-1]
    s = ''.join(filter(str.isalpha, s)).lower()
    found_palindromes = set()
    n = 46
    for i in range(len(s)):
        for j in range(i + n, len(s) + 1):
            potential_palindrome = s[i:j]
            if is_palindrome(potential_palindrome):
                found_palindromes.add(potential_palindrome)
    return found_palindromes