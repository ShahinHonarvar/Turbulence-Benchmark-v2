def palindrome_of_length_at_least_n(s):

    def is_palindrome(sub):
        return sub == sub[::-1]

    def find_palindromes(s, min_length):
        found_palindromes = set()
        s = ''.join(filter(str.isalpha, s)).lower()
        for start in range(len(s)):
            for end in range(start + min_length, len(s) + 1):
                substring = s[start:end]
                if is_palindrome(substring):
                    found_palindromes.add(substring)
        return found_palindromes
    return find_palindromes(s, 66)