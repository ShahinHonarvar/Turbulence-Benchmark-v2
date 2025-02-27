def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    target_substring = s[103:277]
    result = set()
    for length in range(100, 170):
        for i in range(len(target_substring) - length + 1):
            substring = target_substring[i:i + length]
            filtered_substring = ''.join(filter(str.isalpha, substring)).lower()
            if len(filtered_substring) == length and is_palindrome(filtered_substring):
                result.add(filtered_substring)
    return result