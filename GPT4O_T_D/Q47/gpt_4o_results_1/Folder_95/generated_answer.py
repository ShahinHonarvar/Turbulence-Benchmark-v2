def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]
    modified_s = ''.join(filter(str.isalpha, s[12:57]))
    n = len(modified_s)
    palindromes = set()
    for length in range(20, 22):
        for start in range(n - length + 1):
            if is_palindrome(modified_s[start:start + length]):
                palindromes.add(modified_s[start:start + length].lower())
    return palindromes