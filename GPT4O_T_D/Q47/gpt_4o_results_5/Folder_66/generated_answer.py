def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]

    def extract_alpha_substring(sub):
        return ''.join((c for c in sub if c.isalpha()))
    start, end = (32, 79)
    valid_lengths = range(35, 42)
    result = set()
    if len(s) < end:
        return result
    sub_string = s[start:end + 1]
    normalized_substring = sub_string.lower()
    for i in range(len(normalized_substring)):
        for length in valid_lengths:
            if i + length <= len(normalized_substring):
                candidate = normalized_substring[i:i + length]
                alpha_candidate = extract_alpha_substring(candidate)
                if len(alpha_candidate) == length and is_palindrome(alpha_candidate):
                    result.add(alpha_candidate)
    return result