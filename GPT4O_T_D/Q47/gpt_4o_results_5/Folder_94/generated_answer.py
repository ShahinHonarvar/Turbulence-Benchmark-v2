def palindromes_of_specific_lengths(s):

    def is_palindrome(substr):
        return substr == substr[::-1]

    def filter_letters(substr):
        return ''.join(filter(str.isalpha, substr))
    palindromes = set()
    s = s[40:95].lower()
    for length in range(45, 52):
        for start in range(len(s) - length + 1):
            candidate = s[start:start + length]
            filtered_candidate = filter_letters(candidate)
            if len(filtered_candidate) == length and is_palindrome(filtered_candidate):
                palindromes.add(filtered_candidate)
    return palindromes