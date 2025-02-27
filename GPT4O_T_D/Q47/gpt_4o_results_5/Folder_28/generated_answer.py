def palindromes_of_specific_lengths(s):

    def is_palindrome(candidate):
        return candidate == candidate[::-1]
    filtered_substring = ''.join(filter(str.isalpha, s[32:72])).lower()
    palindromes = set()
    for length in range(21, 33):
        for i in range(len(filtered_substring) - length + 1):
            substring = filtered_substring[i:i + length]
            if is_palindrome(substring):
                palindromes.add(substring)
    return palindromes