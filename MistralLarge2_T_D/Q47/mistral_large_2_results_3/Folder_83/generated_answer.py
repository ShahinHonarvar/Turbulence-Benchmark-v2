def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]
    substring = s[75:96]
    palindromes = set()
    for length in range(7, 10):
        for i in range(len(substring) - length + 1):
            sub = substring[i:i + length]
            if is_palindrome(sub) and sub.isalpha():
                palindromes.add(sub.lower())
    return palindromes