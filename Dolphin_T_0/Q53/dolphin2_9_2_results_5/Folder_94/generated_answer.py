def palindrome_of_length_at_least_n(s):

    def find_palindromes_of_length_k(s, k):
        palindromes = set()
        for i in range(len(s) - k + 1):
            if s[i:i + k] == s[i:i + k].lower():
                palindromes.add(s[i:i + k])
        return palindromes
    all_palindromes = set()
    for i in range(41, len(s) + 1):
        all_palindromes |= find_palindromes_of_length_k(s.lower(), i)
    return all_palindromes