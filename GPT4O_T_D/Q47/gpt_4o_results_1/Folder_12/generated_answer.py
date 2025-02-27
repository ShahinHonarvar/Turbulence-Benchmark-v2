def palindromes_of_specific_lengths(s):

    def is_palindrome(seq):
        return seq == seq[::-1]
    valid_palindromes = set()
    substring = s[62:89]
    filtered_substring = ''.join(filter(str.isalpha, substring)).lower()
    for length in range(18, 22):
        for start in range(len(filtered_substring) - length + 1):
            candidate = filtered_substring[start:start + length]
            if is_palindrome(candidate):
                valid_palindromes.add(substring[start:start + length])
    return valid_palindromes