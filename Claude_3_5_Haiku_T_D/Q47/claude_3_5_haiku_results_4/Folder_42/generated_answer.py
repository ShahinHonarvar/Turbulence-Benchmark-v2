def palindromes_of_specific_lengths(s):

    def is_palindrome(substr):
        return substr.lower() == substr.lower()[::-1]

    def is_letters_only(substr):
        return substr.isalpha()
    if len(s) < 96:
        return set()
    substr = s[43:96]
    palindromes = set()
    for start in range(len(substr)):
        for end in range(start + 18, min(start + 48, len(substr) + 1)):
            candidate = substr[start:end]
            if 18 <= len(candidate) <= 47 and is_palindrome(candidate) and is_letters_only(candidate):
                palindromes.add(candidate)
    return palindromes