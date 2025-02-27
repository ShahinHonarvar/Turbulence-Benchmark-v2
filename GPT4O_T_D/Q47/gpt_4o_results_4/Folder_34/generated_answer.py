def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]
    valid_range = s[200:301]
    palindromes = set()
    for length in range(10, 51):
        for start in range(len(valid_range) - length + 1):
            substr = valid_range[start:start + length]
            filtered_substr = ''.join(filter(str.isalpha, substr))
            if len(filtered_substr) == length and is_palindrome(filtered_substr):
                palindromes.add(filtered_substr)
    return palindromes