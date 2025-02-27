def palindrome_of_length_at_least_n(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    s_cleaned = ''.join(filter(str.isalpha, s)).lower()
    result = set()
    for start in range(len(s_cleaned)):
        for end in range(start + 150, len(s_cleaned) + 1):
            substring = s_cleaned[start:end]
            if is_palindrome(substring):
                result.add(substring)
    return result