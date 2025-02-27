def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    start_index = 103
    end_index = 276
    min_length = 100
    max_length = 169
    palindromes_set = set()
    substring = s[start_index:end_index + 1]
    normalized_substring = ''.join(filter(str.isalpha, substring)).lower()
    for length in range(min_length, max_length + 1):
        for i in range(len(normalized_substring) - length + 1):
            sub = normalized_substring[i:i + length]
            if is_palindrome(sub):
                palindromes_set.add(sub)
    return palindromes_set