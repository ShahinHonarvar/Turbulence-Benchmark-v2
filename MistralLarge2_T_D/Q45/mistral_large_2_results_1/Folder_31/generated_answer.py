def palindromes_between_indices(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    substr = ''.join(filter(str.isalpha, s[1:9])).lower()
    palindromes = set()
    for length in range(6, len(substr) + 1):
        for i in range(len(substr) - length + 1):
            sub = substr[i:i + length]
            if is_palindrome(sub):
                palindromes.add(sub)
    return palindromes