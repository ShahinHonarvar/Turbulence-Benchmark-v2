def palindromes_of_specific_lengths(s):

    def is_palindrome(substr):
        return substr == substr[::-1]
    filtered_range = ''.join([ch.lower() for ch in s[16:78] if ch.isalpha()])
    result = set()
    for length in range(43, 48):
        for start in range(len(filtered_range) - length + 1):
            candidate = filtered_range[start:start + length]
            if is_palindrome(candidate):
                result.add(candidate)
    return result