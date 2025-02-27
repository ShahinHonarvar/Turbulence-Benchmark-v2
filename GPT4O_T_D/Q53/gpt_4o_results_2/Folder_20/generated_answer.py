def palindrome_of_length_at_least_n(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    s = ''.join(filter(str.isalpha, s)).lower()
    found_palindromes = set()
    for start in range(len(s)):
        for end in range(start + 66, len(s) + 1):
            if is_palindrome(s[start:end]):
                found_palindromes.add(s[start:end])
    return found_palindromes