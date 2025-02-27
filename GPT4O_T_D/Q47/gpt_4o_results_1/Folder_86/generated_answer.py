def palindromes_of_specific_lengths(s):

    def is_palindrome(substr):
        return substr == substr[::-1]
    substrings = set()
    lower_s = ''.join(filter(str.isalpha, s[30:96].lower()))
    for length in range(34, 56):
        for i in range(len(lower_s) - length + 1):
            candidate = lower_s[i:i + length]
            if is_palindrome(candidate):
                substrings.add(candidate)
    return substrings