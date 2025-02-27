def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    substr = s[34:91].lower()
    valid_palindromes = set()
    for start in range(len(substr)):
        for length in range(14, 40):
            end = start + length
            if end <= len(substr):
                candidate = substr[start:end]
                if candidate.isalpha() and is_palindrome(candidate):
                    valid_palindromes.add(candidate)
    return valid_palindromes