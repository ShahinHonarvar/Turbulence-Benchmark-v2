def palindrome_of_length_at_least_n(s):

    def is_palindrome(s):
        return s.lower() == s.lower()[::-1]
    return set(filter(is_palindrome, s.split()))