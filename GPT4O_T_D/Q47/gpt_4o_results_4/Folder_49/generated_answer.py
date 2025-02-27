def palindromes_of_specific_lengths(s):

    def is_palindrome(substring):
        cleaned = ''.join(filter(str.isalpha, substring)).lower()
        return cleaned == cleaned[::-1]
    result = set()
    lower_bound = 10
    upper_bound = min(101, len(s))
    for start_index in range(lower_bound, upper_bound):
        for length in range(10, 51):
            end_index = start_index + length
            if end_index > upper_bound:
                break
            substring = s[start_index:end_index]
            if is_palindrome(substring):
                cleaned_substring = ''.join(filter(str.isalpha, substring))
                if len(cleaned_substring) == length:
                    result.add(cleaned_substring.lower())
    return result