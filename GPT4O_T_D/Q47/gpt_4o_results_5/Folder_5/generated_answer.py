def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]
    substr = ''.join(filter(str.isalpha, s[63:71]))
    palindromes = set()
    for length in range(4, 6):
        for i in range(len(substr) - length + 1):
            sub = substr[i:i + length]
            if is_palindrome(sub):
                palindromes.add(sub)
    return palindromes