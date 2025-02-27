def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]

    def filter_alpha_chars(text):
        return ''.join((c for c in text if c.isalpha()))
    result = set()
    substring = s[32:72].lower()
    for start in range(len(substring)):
        for length in range(21, 33):
            end = start + length
            if end <= len(substring):
                sub = filter_alpha_chars(substring[start:end])
                sub_length = len(sub)
                if 21 <= sub_length <= 32 and is_palindrome(sub):
                    result.add(sub)
    return result