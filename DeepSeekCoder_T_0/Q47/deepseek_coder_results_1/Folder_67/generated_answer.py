def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]

    def valid_palindromes(sub):
        palindromes = set()
        for length in range(26, 34):
            for i in range(len(sub) - length + 1):
                candidate = sub[i:i + length]
                if candidate.isalpha() and is_palindrome(candidate):
                    palindromes.add(candidate.lower())
        return palindromes
    return valid_palindromes(s[65:100])