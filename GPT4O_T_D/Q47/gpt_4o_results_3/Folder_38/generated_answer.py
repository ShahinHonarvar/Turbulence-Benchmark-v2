def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    result = set()
    start, end = (18, 88)
    for length in range(38, 61):
        for i in range(start, end - length + 1):
            substring = s[i:i + length]
            filtered_substring = ''.join(filter(str.isalpha, substring)).lower()
            if is_palindrome(filtered_substring) and len(filtered_substring) == length:
                result.add(substring)
    return result