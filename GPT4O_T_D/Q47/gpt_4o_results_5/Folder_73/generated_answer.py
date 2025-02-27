def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    result = set()
    substring = s[21:63]
    filtered_substring = ''.join(filter(str.isalpha, substring)).lower()
    for length in range(22, 34):
        for start in range(len(filtered_substring) - length + 1):
            candidate = filtered_substring[start:start + length]
            if is_palindrome(candidate):
                result.add(candidate)
    return result