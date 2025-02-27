def palindromes_of_specific_lengths(s):

    def is_palindrome(substr):
        return substr == substr[::-1]
    s_filtered = ''.join([char for char in s if char.isalpha()])
    s_range = s_filtered[103:277].lower()
    palindromes = set()
    for length in range(100, 170):
        for start in range(len(s_range) - length + 1):
            sub = s_range[start:start + length]
            if is_palindrome(sub):
                palindromes.add(sub)
    return palindromes